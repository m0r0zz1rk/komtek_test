from django.db import transaction
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets

from apps.guide.commons.code.responses import ResponsesClass
from apps.guide.commons.code.error_handling import ErrorHandling
from apps.guide.filters.guides_filter import GuidesFilter
from apps.guide.models import Guides
from apps.guide.serializers.guides_serializers import GuidesSerializer


class GuidesViewSet(viewsets.ViewSet):
    """Получение списка справочников"""
    queryset = Guides.objects.all()
    serializer_class = GuidesSerializer

    param_date = openapi.Parameter('date', openapi.IN_QUERY,
                                   description="Дата начала действия в формате ГГГГ-ММ-ДД",
                                   type=openapi.TYPE_STRING)

    @swagger_auto_schema(
        manual_parameters=[param_date],
        operation_description="Получение списка справочников (+ актуальных на указанную дату)",
        responses={'400': 'Внутреняя ошибка сервера',
                   '200': GuidesSerializer(many=True)}
    )
    def get_guides_list(self, request):
        try:
            with transaction.atomic():
                _filter_qs = GuidesFilter.filter(request, self.queryset)
                serialize = self.serializer_class(_filter_qs, many=True)
                return ResponsesClass.ok_response_dict(
                    {'refbooks': serialize.data}
                )
        except BaseException as ex:
            return ResponsesClass.bad_request_response(
                ErrorHandling.get_traceback()
            )
