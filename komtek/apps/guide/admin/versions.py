from django.contrib import admin

from apps.guide.models import Versions, Elements


class ElementInline(admin.StackedInline):
    """Работа с элементами справочника при редактировании его версии"""
    model = Elements
    extra = 3


@admin.register(Versions)
class VersionsAdmin(admin.ModelAdmin):
    """Работа с моделью версий справочников в административной панели"""
    inlines = [ElementInline]
    list_display = ('guide_code', 'guide_name', 'version', 'date_start_min')

    def guide_code(self, obj) -> str:
        """Получение кода справочника"""
        try:
            return obj.guide.code
        except Exception:
            return '-'

    def guide_name(self, obj) -> str:
        """Получение наименования справочника"""
        try:
            return obj.guide.name
        except Exception:
            return '-'

    def date_start_min(self, obj) -> str:
        """Получение кратого формата даты начала действия версии"""
        try:
            return obj.date_start.strftime('%d.%m.%Y')
        except Exception:
            return '-'

    guide_code.short_description = 'Код справочника'
    guide_name.short_description = 'Наименование справочника'
    date_start_min.short_description = 'Дата начала действия справочника'
