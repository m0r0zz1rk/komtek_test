from django.db import models

from apps.guide.models.base_table import BaseTable
from apps.guide.models.versions import Versions


class Elements(BaseTable):
    """Модель элементов справочников"""
    version = models.ForeignKey(
        Versions,
        to_field='object_id',
        on_delete=models.CASCADE,
        null=False,
        verbose_name='Версия справочника'
    )
    code = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        default='Код элемента',
        verbose_name='Код элемента'
    )
    value = models.CharField(
        max_length=300,
        blank=False,
        null=False,
        default='Значение элемента',
        verbose_name='Значение элемента'
    )

    def __str__(self):
        return f'Элемент "{self.value}" справочника "{self.version.guide.name}" версии {self.version.version}'

    class Meta:
        verbose_name = 'Элемент справочника'
        verbose_name_plural = 'Элементы справочников'
        unique_together = ('version', 'code')