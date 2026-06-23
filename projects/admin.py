from django.contrib import admin

from django.contrib import admin
from .models import Project, ProjectMember


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'datetime_created', 'is_active')
    list_filter = ('is_active', 'datetime_created')
    search_fields = ('name', 'description')
    # filter_horizontal = ('members',)


@admin.register(ProjectMember)
class ProjectMemberAdmin(admin.ModelAdmin):
    list_display = ('project', 'user', 'role', 'datetime_created')
    list_filter = ('role',)
    raw_id_fields = ('project', 'user')