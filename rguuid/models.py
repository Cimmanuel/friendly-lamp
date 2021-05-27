import uuid

from django.db import models
from django.utils import timezone


class RGUUID(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, unique=True, editable=False
    )
    created = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = "RGUUID"
        verbose_name_plural = "RGUUID"
