import uuid

from django.db import models


class BaseTable(models.Model):
    """Базовая модель для приложения"""
    object_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        verbose_name='ID объекта'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата и время создания объекта'
    )

    objects = models.Manager()

    class Meta:
        abstract = True
