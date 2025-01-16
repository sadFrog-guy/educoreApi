from django.db import models

from utils.models import BaseModel


# Create your models here.
class Course(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    # curriculum = models.ForeignKey('Curriculum', on_delete=models.CASCADE, blank=True, null=True)

    duration = models.DurationField(blank=True, null=True)

    INTENSITY_CHOICES = [
        ('base', 'Базовый'),
        ('express', 'Экспресс'),
        ('intensive', 'Интенсивный'),
    ]

    intensity = models.CharField(
        max_length=100,
        choices=INTENSITY_CHOICES,
        default='base',
        verbose_name="Интенсивность"
    )

    def get_duration_in_days(self):
        """Возвращает продолжительность в днях, если поле не пустое"""
        if self.duration:
            return self.duration.days
        return 0  # если duration None, возвращаем 0 дней

    get_duration_in_days.short_description = 'Продолжительность в днях'

    def get_duration_in_weeks(self):
        """Возвращает продолжительность в неделях"""
        if self.duration:
            return self.duration.days // 7
        return 0  # если duration None, возвращаем 0 недель

    get_duration_in_weeks.short_description ='Продолжительность в неделях'

    def get_duration_in_months(self):
        """Возвращает продолжительность в месяцах (приближенно 30 дней в месяце)"""
        if self.duration:
            return self.duration.days // 30
        return 0  # если duration None, возвращаем 0 месяцев

    get_duration_in_months.short_description = 'Продолжительность в месяцах'

    def __str__(self):
        return f"{self.name} | {self.intensity}"