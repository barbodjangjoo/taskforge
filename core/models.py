from django.db import models
from django.conf import settings


class BaseModel(models.Model):

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="%(class)s_created_by",
    )
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True
        ordering = ['-datetime_created']

    def __str__(self):
        return f"{self.__class__.__name__} - {self.pk}"
    
    