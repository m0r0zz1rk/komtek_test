import datetime
from typing import Optional


class DateUtils:
    """Методы для работы с датой"""

    @staticmethod
    def convert_to_date(object) -> Optional[datetime.date]:
        """Преобразование полученного объекта в дату"""
        try:
            return datetime.datetime.strptime(object, '%Y-%m-%d')
        except ValueError:
            return None