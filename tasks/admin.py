from django.contrib import admin
from .models import Board, Column, Task


@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = ('name', 'project', 'is_default', 'datetime_created')


@admin.register(Column)
class ColumnAdmin(admin.ModelAdmin):
    list_display = ('name', 'board', 'position')
    list_editable = ('position',)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'column', 'assignee', 'priority', 'due_date')
    list_filter = ('priority', 'column')
    search_fields = ('title', 'description')
    raw_id_fields = ('project', 'column', 'assignee')