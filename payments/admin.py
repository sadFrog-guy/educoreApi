from django.contrib import admin

from .models import Payment


@admin.register(Payment)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('student', 'amount', 'group')