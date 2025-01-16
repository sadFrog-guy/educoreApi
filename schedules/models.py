from datetime import timedelta, datetime

from dateutil.relativedelta import relativedelta
from django.core.exceptions import ValidationError
from django.db import models
from sqlparse.engine.grouping import group

from groups. models import Group
from lessons.models import Lesson
from teachers. models import Teacher
from rooms. models import Room
from utils.models import BaseModel


class WeeklySchedule(BaseModel):
    DAYS_OF_WEEK = [
        (0, "Monday"),
        (1, "Tuesday"),
        (2, "Wednesday"),
        (3, "Thursday"),
        (4, "Friday"),
        (5, "Saturday"),
        (6, "Sunday"),
    ]

    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name="weekly_schedules", verbose_name="Group")
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name="weekly_schedules", verbose_name="Teacher")
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="weekly_schedules", verbose_name="Room")
    day_of_week = models.IntegerField(choices=DAYS_OF_WEEK, verbose_name="Day of Week")
    start_time = models.TimeField(verbose_name="Start Time")
    end_time = models.TimeField(verbose_name="End Time")

    class Meta:
        verbose_name = "Weekly Schedule"
        verbose_name_plural = "Weekly Schedules"
        ordering = ["day_of_week", "start_time"]
        constraints = [
            models.UniqueConstraint(
                fields=["room", "day_of_week", "start_time"],
                name="unique_schedule",
                # condition=models.Q(is_active=True)  # Уникальность только для активных записей
            )
        ]

    def create_lessons_from_schedule(self):
        """Создает уроки на основе регулярного расписания для текущего объекта Schedule."""

        # Текущая дата, на основании которой будут создаваться уроки
        start_date = datetime.now().date()  # Начинаем с текущей даты
        end_date = self.get_last_day_of_next_month(start_date)  # Дата окончания - последний день следующего месяца

        current_date = start_date

        # Определим, в какой день недели начинается первый урок
        while current_date.weekday() != self.day_of_week:
            current_date += timedelta(days=1)

        # Создаем уроки, начиная с даты, соответствующей day_of_week, до конца месяца
        while current_date <= end_date:
            # Генерируем время начала и окончания урока для этого дня
            lesson_start_time = self.start_time
            lesson_end_time = self.end_time

            # Проверяем, если урок с таким временем и учителем уже существует (чтобы избежать дублирования)
            if not Lesson.objects.filter(
                    teacher=self.teacher,
                    room=self.room,
                    date=current_date,
                    start_time=lesson_start_time
            ).exists():
                # Создаем новый урок
                Lesson.objects.create(
                    branch=self.group.branch,
                    group=self.group,
                    teacher=self.teacher,
                    room=self.room,
                    lesson_type='regular',
                    date=current_date,
                    start_time=lesson_start_time,
                    end_time=lesson_end_time
                )

            # Переходим к следующему дню недели
            current_date += timedelta(weeks=1)

    def get_last_day_of_next_month(self, current_date):
        """Возвращает последний день месяца, следующего за текущим месяцем."""

        # Первый день следующего месяца
        start_of_next_month = current_date.replace(day=1) + relativedelta(months=+1)

        # Первый день месяца, который идет после следующего месяца
        start_of_month_after_next = start_of_next_month + relativedelta(months=+1)

        # Получаем последний день следующего месяца
        end_of_next_month = start_of_month_after_next - relativedelta(days=1)

        return end_of_next_month

    def save(self, *args, **kwargs):
        # Сначала сохраняем сам объект Schedule
        super().save(*args, **kwargs)

        # Логика для создания уроков из этого расписания
        self.create_lessons_from_schedule()

    def clean(self):
        # Проверка на пересечение уроков для учителя
        overlapping_lessons = WeeklySchedule.objects.filter(
            teacher=self.teacher,
            day_of_week=self.day_of_week,
            start_time__lt=self.end_time,
            end_time__gt=self.start_time
        ).exclude(id=self.id)  # Исключаем текущий урок, если он уже существует в базе

        if overlapping_lessons.exists():
            raise ValidationError("The teacher is already teaching at this time.")

    def __str__(self):
        return f"{self.group.name} - {self.get_day_of_week_display()} {self.start_time} - {self.end_time}"


