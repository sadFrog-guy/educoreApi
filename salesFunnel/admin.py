from django.contrib import admin

from .models import SalesFunnelStage, Lead, FunnelAction

class SalesFunnelStageAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')
    list_filter = ('order',)
    search_fields = ('name',)
    ordering = ['order']
    list_per_page = 20

class LeadAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'current_stage', 'created_at', 'updated_at')
    list_filter = ('current_stage', 'created_at', 'updated_at')
    search_fields = ('first_name', 'last_name', 'email', 'phone')
    ordering = ['created_at']
    list_per_page = 20

class FunnelActionAdmin(admin.ModelAdmin):
    list_display = ('lead', 'stage', 'created_at', 'note')
    list_filter = ('stage', 'created_at',)
    search_fields = ('lead__first_name', 'lead__last_name', 'stage__name', 'note')
    ordering = ['created_at']
    list_per_page = 20

admin.site.register(SalesFunnelStage, SalesFunnelStageAdmin)
admin.site.register(Lead, LeadAdmin)
admin.site.register(FunnelAction, FunnelActionAdmin)