from uuid import UUID

from rest_framework import filters
from apps.guide.commons.code.dict import DictUtils


class ElementsFilter(filters.BaseFilterBackend):
    """Класс фильтрации queryset c элементами справочника"""

    @staticmethod
    def filter(request, queryset, guide_id):
        if isinstance(guide_id, UUID):
            qs = queryset.filter(version__guide__object_id=guide_id)
        else:
            return None
        du = DictUtils()
        if DictUtils.exist_key_in_dict('version', request.GET):
            qs = qs.filter(version__version=du.get_str_value_in_dict_by_key('version', request.GET))
        return qs
