from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from . import models

@admin.register(models.CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'full_name', 'username', 'is_staff', 'is_active', 'date_joined')
    search_fields = ('email', 'username', 'first_name', 'last_name', 'full_name')
    ordering = ('-date_joined',)
    
    fieldsets = UserAdmin.fieldsets + (
        ('extra information', {'fields': ('avatar', 'bio', 'is_online', 'last_activity')}),
    )
