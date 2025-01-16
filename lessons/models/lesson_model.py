from django.core.exceptions import ValidationError
from django.db import models
from groups. models import Group
from teachers. models import Teacher
from rooms. models import Room
from utils.models import BaseModel


class Lesson(BaseModel):
    """Модель урока."""
    LESSON_TYPE_CHOICES = [
        ("regular", "Regular"),
        ("trial", "Trial"),
        ("rescheduled", "Rescheduled"),
        ("one_time", "One-Time"),
        ("other", "Other"),
    ]
    STATUS_CHOICES = [
        ('scheduled', 'Запланирован'),
        ('in_progress', 'В процессе'),
        ('completed', 'Проведён'),
        ('canceled', 'Отменён'),
        ('not_held', 'Не состоялся'),
        ('rescheduled', 'Перенесён'),
    ]
    title = models.CharField(max_length=100, null=True, blank=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name="lessons", verbose_name="Group")
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name="lessons", verbose_name="Teacher")
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="lessons", verbose_name="Room")
    date = models.DateField(verbose_name="Date")
    start_time = models.TimeField(verbose_name="Start Time")
    end_time = models.TimeField(verbose_name="End Time")
    lesson_type = models.CharField(max_length=20, choices=LESSON_TYPE_CHOICES, default="regular", verbose_name="Lesson Type")
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='scheduled',  # По умолчанию статус "Запланирован"
        verbose_name="Статус"
    )
    previous_date = models.DateTimeField(
        blank=True, null=True, verbose_name="Предыдущая дата",
        help_text="Если урок перенесён, укажите дату, с которой он был перенесён."
    )

    # Если выбран тип "Other", то можно ввести дополнительное описание
    other_description = models.CharField(max_length=255, blank=True, null=True, verbose_name="Other Description")

    class Meta:
        verbose_name = "Lesson"
        verbose_name_plural = "Lessons"
        ordering = ["date", "start_time"]
        constraints = [
            models.UniqueConstraint(
                fields=["room", "date", "start_time"],
                name="unique_lesson",
            )
        ]

    # condition=models.Q(is_active=True)  # Уникальность только для активных записей

    def clean(self):
        # Проверка на пересечение уроков для учителя
        overlapping_lessons = Lesson.objects.filter(
            teacher=self.teacher,
            date=self.date,
            start_time__lt=self.end_time,
            end_time__gt=self.start_time
        ).exclude(id=self.id)  # Исключаем текущий урок, если он уже существует в базе

        if overlapping_lessons.exists():
            raise ValidationError("The teacher is already teaching at this time.")

        # Валидация для "Other" типа урока
        if self.lesson_type == "other" and not self.other_description:
            raise ValidationError(
                {'other_description': 'You must provide a description for "Other" lesson type.'}
            )

    def __str__(self):
        return f"{self.group.name} - {self.date} {self.start_time} - {self.end_time}"