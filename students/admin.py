from django.contrib import admin
from .models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'groups_count')

admin.site.register(Student, StudentAdmin)