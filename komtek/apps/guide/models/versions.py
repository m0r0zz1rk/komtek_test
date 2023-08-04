import datetime

from django.db import models

from apps.guide.models.base_table import BaseTable
from apps.guide.models.guides import Guides


class Versions(BaseTable):
    """Модель версий справочников"""
    guide = models.ForeignKey(
        Guides,
        to_field='object_id',
        on_delete=models.CASCADE,
        null=False,
        verbose_name='Справочник'
    )
    version = models.CharField(
        max_length=50,
        blank=False,
        null=False,
        default='Версия справочника',
        verbose_name='Версия справочника'
    )
    date_start = models.DateField(
        default=datetime.date.today,
        verbose_name='Дата начала действия версии'
    )

    def __str__(self):
        return f'Версия {self.version} справочника "{self.guide.name}"'

    class Meta:
        verbose_name = 'Версия справочника'
        verbose_name_plural = 'Версии справочников'
        unique_together = ('guide', 'version', 'date_start')
