from django.contrib import admin

from .models import Lesson, LessonStudent


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ("group", "teacher", "room", "date", "start_time", "end_time", "lesson_type", 'status', 'previous_date')
    list_filter = ("lesson_type", "date", "teacher", "room", 'status')
    search_fields = ("group__name", "teacher__name", "room__name")

@admin.register(LessonStudent)
class LessonStudentAdmin(admin.ModelAdmin):
    list_display = ("lesson", "student")
    search_fields = ("lesson", "student")
