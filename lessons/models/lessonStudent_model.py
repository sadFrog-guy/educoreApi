from django.db import models

from students.models import Student
from .lesson_model import Lesson
from utils.models import BaseModel


class LessonStudent(BaseModel):
    STATUS_CHOICES = [
        ('pending', 'Ожидается'),
        ('present', 'Присутствует'),
        ('absent', 'Отсутствует без причины'),
        ('sick', 'Отсутствует по болезни'),
        ('late', 'Опоздал'),
        ('excused', 'Освобожден'),
        ('removed', 'Удалён'),
        ('other', 'Другое'),
    ]
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name="students", verbose_name="Lesson")
    student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name="lessons", verbose_name="Student")
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending',  # По умолчанию статус "Ожидается"
        verbose_name="Статус"
    )
    reason = models.TextField(blank=True, null=True, verbose_name="Причина (если выбрано ""Другое"")")
    timestamp = models.DateTimeField(null=True, blank=True,verbose_name="Время записи")

    def __str__(self):
        return f"{self.student} - {self.lesson}: {self.get_status_display()}"

    def __str__(self):
        return self.student.first_name
