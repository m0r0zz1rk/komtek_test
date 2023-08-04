from django.contrib import admin

from apps.guide.commons.versions_actions import VersionsActions
from apps.guide.models import Guides, Versions


class VersionInline(admin.StackedInline):
    """Работа с версиями справочника при его редактировании"""
    model = Versions
    extra = 3


@admin.register(Guides)
class GuidesAdmin(admin.ModelAdmin):
    """Работа с моделью справочников в административной панели"""
    inlines = [VersionInline]
    list_display = ('object_id', 'code', 'name', 'actual_version', 'date_version')

    def actual_version(self, obj) -> str:
        """Получение актуальной версии"""
        return VersionsActions.get_guide_curr_version(obj.object_id, 'version')

    def date_version(self, obj) -> str:
        """Получение даты начала действия актуальной версии"""
        return VersionsActions.get_guide_curr_version(obj.object_id, 'date')

    actual_version.short_description = 'Текущая версия'
    date_version.short_description = 'Дата начала действия версии'
