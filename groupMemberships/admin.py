from django.contrib import admin
from .models import GroupMembership

from .models import GroupMembership

class GroupMembershipInline(admin.TabularInline):
    model = GroupMembership
    extra = 1  # Количество пустых форм, которые будут показаны

class GroupMembershipAdmin(admin.ModelAdmin):
    list_display = ("__str__",)

admin.site.register(GroupMembership, GroupMembershipAdmin)