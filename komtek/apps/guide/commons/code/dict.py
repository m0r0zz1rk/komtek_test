from typing import Optional


class DictUtils:
    """Словарные валидаторы и методы"""

    @staticmethod
    def dict_is_empty(d: dict) -> bool:
        """Проверка на пустой словарь"""
        if not bool(d):
            return True
        else:
            return False

    @staticmethod
    def exist_key_in_dict(key: str, data: dict) -> bool:
        """Проверка нахождения ключа в словаре"""
        if data is None:
            return False
        if key in data.keys():
            return True
        else:
            return False

    def get_str_value_in_dict_by_key(self,
                                     key: str,
                                     data: dict,
                                     default=None) -> Optional[str]:
        """Получение строки по ключу в словаре"""
        if self.exist_key_in_dict(key, data):
            value = data[key]
            if value is not None:
                if isinstance(value, str):
                    if value != 'null':
                        return value
                    return None
                else:
                    try:
                        return str(value)
                    except ValueError:
                        return default
            return None
        return default

    @staticmethod
    def convert_obj_to_dict(obj):
        """Конвертирование объекта в словарь"""
        try:
            return dict(obj)
        except ValueError:
            return None
