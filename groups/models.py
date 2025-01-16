from django.db import models

from courses.models import Course
from utils.models import BaseModel


class Group(BaseModel):
    name = models.CharField(max_length=120)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, blank=True, null=True)

    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    STATUS_CHOICES = [
        ('RECRUITING', 'Набирается'),
        ('ACTIVE', 'Учится'),
        ('COMPLETED', 'Завершена'),
        ('INACTIVE', 'Неактивна'),
    ]

    status = models.CharField(
        max_length=100,
        choices=STATUS_CHOICES,
        default='RECRUITING',  # Статус по умолчанию
    )

    def students_count(self):
        return self.group_members.count()

    def teachers_names(self):
        all_teacher = self.group_teachers.all()
        teachers = ''
        for teacher in all_teacher:
            teachers += teacher.__str__()
        return teachers

    def __str__(self):
        return str(f'{self.name} | {self.course}')