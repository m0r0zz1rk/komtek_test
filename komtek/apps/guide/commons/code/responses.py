from rest_framework import status
from rest_framework.response import Response


class ResponsesClass:
    """Класс для генерации ответов на запросы"""

    @staticmethod
    def bad_request_response(message) -> Response:
        """Генерация ответа с кодом 200 и ошибкой error"""
        return Response(
            {'error': message},
            status=status.HTTP_400_BAD_REQUEST
        )

    @staticmethod
    def ok_response_dict(d: dict) -> Response:
        """Генерация ответа с кодом 200 и телом полученного словаря"""
        return Response(
            d,
            status=status.HTTP_200_OK
        )

    @staticmethod
    def ok_response_no_data() -> Response:
        """Генерация ответа с кодом 200 без данных"""
        return Response(status=status.HTTP_200_OK)

    @staticmethod
    def response_object_not_found() -> Response:
        """Генерация ответа с кодом 404 без данных"""
        return Response(status=status.HTTP_404_NOT_FOUND)