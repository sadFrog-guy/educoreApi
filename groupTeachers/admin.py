from django.contrib import admin

from .models import GroupTeacher

class GroupTeachersInline(admin.TabularInline):
    model = GroupTeacher
    extra = 1  # Количество пустых форм, которые будут показаны

admin.site.register(GroupTeacher)