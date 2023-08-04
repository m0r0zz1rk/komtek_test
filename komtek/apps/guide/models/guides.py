from django.db import models

from apps.guide.models.base_table import BaseTable


class Guides(BaseTable):
    """Модель Справочник"""
    code = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        default='Код нового справочника',
        unique=True,
        verbose_name='Код справочника'
    )
    name = models.CharField(
        max_length=300,
        blank=False,
        null=False,
        verbose_name='Наименование справочника',
        default='Наименование справочника',
    )
    description = models.TextField(
        verbose_name='Описание'
    )

    def __str__(self):
        return f'Справочник "{self.name}"'

    class Meta:
        verbose_name = 'Справочник'
        verbose_name_plural = 'Справочники'
