from django.contrib import admin

from groupTeachers.admin import GroupTeachersInline
from groupMemberships.admin import GroupMembershipInline
from .models import Group

class GroupAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'status', 'students_count', 'teachers_names')  # Добавляем отображение количества учеников
    inlines = [GroupMembershipInline, GroupTeachersInline]

admin.site.register(Group, GroupAdmin)