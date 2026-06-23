from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import BaseModel
from projects.models import Project
from accounts.models import CustomUser

class Board(BaseModel):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='boards')
    name = models.CharField(_('name'), max_length=255)
    is_default = models.BooleanField(default=False)

    class Meta:
        verbose_name = _('Board')
        verbose_name_plural = _('Boards')


class Column(BaseModel):
    
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='columns')
    name = models.CharField(_('Column name'), max_length=100)
    position = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['position']
        verbose_name = _('Column')
        verbose_name_plural = _('Columns')

class Task(BaseModel):
    
    PRIORITY_CHOICES = (
        ('low', _('Low')),
        ('medium', _('Medium')),
        ('high', _('High')),
        ('urgent', _('Urgent'))
    )

    title = models.CharField(_('title'), max_length=255)
    description = models.TextField(_('description'), blank=True)
    
    column = models.ForeignKey(Column, on_delete=models.CASCADE, related_name='tasks')
    assignee = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_tasks')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')

    priority = models.CharField(_('priority'), max_length=20, choices=PRIORITY_CHOICES, default='medium')
    due_date = models.DateTimeField(_('Due Date'), null=True, blank=True)
    labels = models.JSONField(_('Labels'), default=list, blank=True)

    class Meta:
        verbose_name = _('task')
        verbose_name_plural = _('tasks')
        ordering = ['-datetime_created']
