from django.contrib import admin

from apps.guide.models import Elements


@admin.register(Elements)
class ElementsAdmin(admin.ModelAdmin):
    """Работа с моделью элементов справочника в административной панели"""
    list_display = ('guide_name', 'guide_version', 'code', 'value')

    def guide_name(self, obj) -> str:
        """Получение наименования справочника"""
        try:
            return obj.version.guide.name
        except Exception:
            return '-'

    def guide_version(self, obj) -> str:
        """Получение версии справочника"""
        try:
            return obj.version.version
        except Exception:
            return '-'

    guide_name.short_description = 'Наименование справочника'
    guide_version.short_description = 'Версия справочника'
