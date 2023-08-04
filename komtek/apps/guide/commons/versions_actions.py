import datetime
from uuid import UUID

from apps.guide.models import Versions


class VersionsActions:
    """Класс методов для работы с версиями справочников"""

    @staticmethod
    def get_guide_curr_version(guide_id: UUID, field: str) -> str:
        """Получение текущей версии справочника или даты начала действия версии"""
        if Versions.objects.filter(guide_id=guide_id).exists():
            rec = Versions.objects.filter(guide_id=guide_id).\
                filter(date_start__lte=datetime.date.today()).order_by('-date_start').first()
            if field == 'version':
                return rec.version
            else:
                return rec.date_start.strftime('%d.%m.%Y')
        return '-'

    @staticmethod
    def get_guides_id_versions_lte_date(date) -> list:
        """Получение списка ID справочников, у которых дата начала версий меньше или равна полученной"""
        guides = []
        if isinstance(date, datetime.date):
            guides = [version.guide.object_id for version in Versions.objects.filter(date_start__lte=date)]
        return guides
