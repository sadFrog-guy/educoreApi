import traceback
from lib2to3.pgen2.tokenize import group
from msilib.schema import Property

from django.db import models

from payments.models import Payment
from students.models import Student
from groups.models import Group
from utils.calculate_full_months_excluding_partial import calculate_full_months_excluding_partial
from utils.models import BaseModel
from datetime import datetime, timedelta
from django.db.models import Sum


class GroupMembership(BaseModel):
    STATUS_CHOICES = [
        ('pending_approval', 'Ожидает подтверждения'),  # Заявка подана, но не утверждена
        ('enrolled', 'Записан'),  # Записан на курс
        ('studying', 'Обучается'),  # Активно учится
        ('paused', 'На паузе'),  # Обучение временно приостановлено
        ('completed', 'Завершил курс'),  # Успешно закончил курс
        ('not_completed', 'Не завершил'),  # Не завершил обучение
        ('withdrawn', 'Отказался'),  # Сам отказался от курса
        ('expelled', 'Исключён'),  # Удалён из курса
    ]
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='group_memberships')
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='group_members')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending_approval',  # По умолчанию "Ожидает подтверждения"
        verbose_name="Статус"
    )
    enrolled_date = models.DateField(blank=True, null=True, verbose_name="Дата записи на курс")
    completion_date = models.DateField(blank=True, null=True, verbose_name="Дата завершения")
    notes = models.TextField(blank=True, null=True, verbose_name="Примечания")


    # balance = models.DecimalField(max_digits=10, decimal_places=2, default=0, blank=True, null=True)
    first_month_payment = models.DecimalField(max_digits=10, decimal_places=2, default=0, blank=True, null=True)
    last_month_payment = models.DecimalField(max_digits=10, decimal_places=2, default=0, blank=True, null=True)

    def total_payments(self):
        # traceback.print_stack()
        amount = Payment.objects.filter(student=self.student, group=self.group).aggregate(Sum('amount'))['amount__sum']
        return amount or 0

    @property
    def balance(self):
        total_paid = self.total_payments()

        if self.group.status == 'ACTIVE':
            start_date = self.group.start_date
            end_date = self.group.end_date

            months_data = calculate_full_months_excluding_partial(start_date, end_date)
            months = months_data['count']
            balance = months * (-self.price) + (-self.first_month_payment)

            # Добавляем оплату за последний месяц, если нужно
            if months_data['is_last_month']:
                balance += (-self.last_month_payment)

            # Возвращаем разницу
            return balance + total_paid
        else:
            return total_paid

    class Meta:
        unique_together = ('student', 'group')

    def __str__(self):
        return f'{self.group} | {self.student} | {self.balance}'

