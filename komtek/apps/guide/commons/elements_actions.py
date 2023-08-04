class ElementsActions:
    """Класс методов для работы с элементами справочников"""

    @staticmethod
    def check_element_exist(qs, code, value) -> bool:
        """Проверка существующего элемента по коду и значению в полученном queryset"""
        print(code)
        print(value)
        try:
            return qs.filter(code=code).filter(value=value).exists()
        except Exception:
            return False