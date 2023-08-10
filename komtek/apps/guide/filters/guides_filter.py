from rest_framework import filters

from apps.guide.commons.code.date import DateUtils
from apps.guide.commons.code.dict import DictUtils
from apps.guide.commons.versions_actions import VersionsActions


class GuidesFilter(filters.BaseFilterBackend):
    """Класс фильтрации queryset со справочниками"""

    @staticmethod
    def filter(request, queryset):
        qs = queryset
        if DictUtils.exist_key_in_dict('date', request.GET):
            get_date = DateUtils.convert_to_date(du.get_str_value_in_dict_by_key('date', request.GET))
            if get_date:
                guides = VersionsActions.get_guides_id_versions_lte_date(
                    get_date
                )
                qs = qs.filter(object_id__in=guides)
        return qs
