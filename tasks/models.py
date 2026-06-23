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
        