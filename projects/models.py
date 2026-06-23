from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import BaseModel
from accounts.models import CustomUser

class Project(BaseModel):

    name = models.CharField(_('name'), max_length=255)
    description = models.TextField(_('description'), blank=True)
    owner = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='owned_projects',
        verbose_name=_('owner')
    )
    members = models.ManyToManyField(
        CustomUser,
        through='ProjectMember',
        related_name='projects',
        verbose_name=_('project members')
    )

class ProjectMember(BaseModel):

    ROLE_CHOICES = (
        ('admin', _('Admin')),
        ('member', _('Member')),
        ('viewer', _('Viewer'))
    )

    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    role = models.CharField(_('role'), max_length=6, choices=ROLE_CHOICES, default='member')
    
    class Meta:
        unique_together = ('project', 'user')
        verbose_name = _('Project Member')
        verbose_name_plural = _('Project Members')
