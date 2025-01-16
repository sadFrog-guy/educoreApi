from django.db import models

from lessons.models import Lesson
from groups.models import Group
from students.models import Student
from datetime import date, timedelta

from utils.models import BaseModel


class Payment(BaseModel):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

# class Subscription(BaseModel):
#     student = models.ForeignKey(Student, on_delete=models.CASCADE)
#     start_date = models.DateField()  # Дата начала абонемента
#     end_date = models.DateField()    # Дата окончания абонемента
#     amount_per_month = models.DecimalField(max_digits=10, decimal_places=2)  # Сумма за месяц
#     last_payment_date = models.DateField()  # Последняя дата платежа
#     next_payment_date = models.DateField()  # Дата следующего платежа
#
#     @property
#     def is_overdue(self):
#         """Проверка на просрочку"""
#         return self.next_payment_date < date.today()
#
#     @property
#     def days_until_due(self):
#         """Количество дней до следующего платежа"""
#         return (self.next_payment_date - date.today()).days
#
#     def __str__(self):
#         return f"{self.student} - {self.next_payment_date}"
#
# class LessonPayment(BaseModel):
#     student = models.ForeignKey(Student, on_delete=models.CASCADE)
#     lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
#     amount = models.DecimalField(max_digits=10, decimal_places=2)  # Сумма за урок
#     payment_date = models.DateField(auto_now_add=True)
#     is_paid = models.BooleanField(default=False)  # Признак того, что урок оплачен
#
#     def __str__(self):
#         return f"Payment for {self.lesson.title} by {self.student}"
#
# class Payment(BaseModel):
#     student = models.ForeignKey(Student, on_delete=models.CASCADE)
#     amount = models.DecimalField(max_digits=10, decimal_places=2)  # Сумма платежа
#     payment_date = models.DateField(auto_now_add=True)  # Дата платежа
#     payment_type = models.CharField(
#         max_length=20,
#         choices=[('subscription', 'Абонемент'), ('lesson', 'Урок')],
#         default='subscription'
#     )
#
#     def make_lesson_payment(self):
#         """Логика для обработки платежа за урок."""
#         # Для разового платежа на урок, мы должны обновить уроки студента
#         lessons = self.student.lessons.filter(is_paid=False, lesson_date__lte=self.payment_date)
#
#         # Сопоставление платежа с уроками
#         for lesson in lessons:
#             if self.amount >= lesson.price:
#                 lesson.is_paid = True
#                 self.amount -= lesson.price  # Уменьшаем оставшуюся сумму
#                 lesson.save()
#
#             if self.amount <= 0:
#                 break  # Если сумма платежа исчерпана, выходим
#
#     def make_subscription_payment(student, amount_paid):
#         subscription = Subscription.objects.get(student=student)
#         if subscription.is_overdue:
#             # Логика для того, как обрабатывать просрочку (например, начисление штрафов)
#             pass
#
#         subscription.last_payment_date = date.today()
#         subscription.next_payment_date = subscription.last_payment_date + timedelta(days=30)
#         subscription.save()
#
#         # Добавляем запись в таблицу Payment
#         Payment.objects.create(student=student, amount=amount_paid, payment_type='subscription')
#
#     def save(self, *args, **kwargs):
#         # Сохраняем платёж
#         super().save(*args, **kwargs)
#
#         # Если это платеж за абонемент
#         if self.payment_type == 'subscription':
#             subscription = self.subscription
#             if subscription:
#                 subscription.last_payment_date = self.payment_date
#                 subscription.next_payment_date = self.payment_date + timedelta(days=30)  # Следующий платёж через месяц
#                 if subscription.is_overdue:
#                     # Логика для обработки просрочки, например, начисление штрафа
#                     pass
#                 subscription.save()
#
#         # Если это платеж за урок
#         elif self.payment_type == 'lesson':
#             self.make_lesson_payment()  # Вызов функции для обработки оплаты за урок
#
#     def __str__(self):
#         return f"{self.student} - {self.amount} on {self.payment_date}"



# Теперь, для каждого ученика мы можем отслеживать, есть ли у него просрочка по абонементу или платежам за уроки.
# Мы добавим методы для уведомления о близкой дате платежа и просрочках.
# Пример логики для уведомлений:
# def send_due_payment_notifications():
#     # Получаем всех студентов с просроченными платежами по абонементу
#     overdue_subscriptions = Subscription.objects.filter(next_payment_date__lt=date.today())
#
#     for subscription in overdue_subscriptions:
#         if subscription.is_overdue:
#             # Логика уведомления (например, отправка email или SMS)
#             print(f"Ученик {subscription.student.full_name} имеет просрочку по абонементу.")
#
#     # Получаем студентов, у которых скоро будет платеж
#     upcoming_subscriptions = Subscription.objects.filter(next_payment_date__lte=date.today() + timedelta(days=7))
#
#     for subscription in upcoming_subscriptions:
#         if subscription.days_until_due <= 7:
#             # Логика уведомления (например, отправка email или SMS)
#             print(f"Ученик {subscription.student.full_name} должен заплатить через {subscription.days_until_due} дней.")

# Обновление информации о следующем платеже:
# Каждый раз, когда студент платит, обновляется дата следующего платежа:
# def make_subscription_payment(student, amount_paid):
#     subscription = Subscription.objects.get(student=student)
#     if subscription.is_overdue:
#         # Логика для того, как обрабатывать просрочку (например, начисление штрафов)
#         pass
#
#     subscription.last_payment_date = date.today()
#     subscription.next_payment_date = subscription.last_payment_date + timedelta(days=30)
#     subscription.save()
#
#     # Добавляем запись в таблицу Payment
#     Payment.objects.create(student=student, amount=amount_paid, payment_type='subscription')

# Отслеживание долгов за уроки
# Для того чтобы отслеживать долги по урокам, используем модель LessonPayment. Когда ученик платит за урок, это фиксируется в таблице LessonPayment.
# def make_lesson_payment(student, lesson, amount_paid):
#     lesson_payment = LessonPayment.objects.get(student=student, lesson=lesson)
#
#     if not lesson_payment.is_paid:
#         lesson_payment.amount = amount_paid
#         lesson_payment.is_paid = True
#         lesson_payment.save()
#
#     # Добавляем запись в таблицу Payment
#     Payment.objects.create(student=student, amount=amount_paid, payment_type='lesson')


# Уведомления и регулярные задачи
# Для уведомлений можно использовать Django Celery или планировщик задач,
# чтобы регулярно проверять, у кого просроченные платежи или кто должен оплатить в ближайшее время.