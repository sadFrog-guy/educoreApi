from django.contrib import admin
from .models import WeeklySchedule


@admin.register(WeeklySchedule)
class WeeklyScheduleAdmin(admin.ModelAdmin):
    list_display = ("group", "teacher", "room", "day_of_week", "start_time", "end_time")
    list_filter = ("day_of_week", "room", "teacher")
    search_fields = ("group__name", "teacher__name", "room__name")
