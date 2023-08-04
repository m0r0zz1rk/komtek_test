from django.db import transaction
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets

from apps.guide.commons.code.responses import ResponsesClass
from apps.guide.commons.code.error_handling import ErrorHandling
from apps.guide.commons.code.rest import RestUtils
from apps.guide.commons.elements_actions import ElementsActions
from apps.guide.filters.elements_filter import ElementsFilter
from apps.guide.models import Elements
from apps.guide.serializers.elements_serializer import ElementsSerializer


class ElementsViewSet(viewsets.ViewSet):
    """Элементы справочника"""
    queryset = Elements.objects.all()
    serializer_class = ElementsSerializer

    param_version = openapi.Parameter(
        'version', openapi.IN_QUERY,
        description="Версия справочника",
        type=openapi.TYPE_STRING
    )
    param_guide_id = openapi.Parameter(
        'guide_id', openapi.IN_QUERY,
        description="ID справочника",
        type=openapi.TYPE_STRING,
        required=True
    )
    param_code = openapi.Parameter(
        'code', openapi.IN_QUERY,
        description="Код элемента справочника",
        type=openapi.TYPE_STRING,
        required=True
    )
    param_value = openapi.Parameter(
        'value', openapi.IN_QUERY,
        description="Значение элемента справочника",
        type=openapi.TYPE_STRING,
        required=True
    )

    @swagger_auto_schema(
        manual_parameters=[param_guide_id, param_version],
        operation_description="Получение элементов заданного справочника",
        responses={'400': 'Внутреняя ошибка сервера',
                   '200': ElementsSerializer(many=True)}
    )
    def get_elements_list(self, request, **kwargs):
        try:
            with transaction.atomic():
                _filter_qs = ElementsFilter.filter(request, self.queryset, kwargs['guide_id'])
                serialize = self.serializer_class(_filter_qs, many=True)
                return ResponsesClass.ok_response_dict(
                    {'elements': serialize.data}
                )
        except BaseException:
            return ResponsesClass.bad_request_response(
                ErrorHandling.get_traceback()
            )

    @swagger_auto_schema(
        manual_parameters=[param_guide_id, param_code, param_value, param_version],
        operation_description="Получение элементов заданного справочника",
        responses={'400': 'Ошибка валидации запроса',
                   '404': 'Элемент не найден',
                   '200': 'Элемент существует'}
    )
    def check_element_exist(self, request, **kwargs):
        params = [
            'code',
            'value',
        ]
        ru = RestUtils()
        if not ru.validate_params_to_list(request, params):
            return ResponsesClass.bad_request_response(
                'Ошибка валидации тела запроса. Проверьте данные'
            )
        try:
            with transaction.atomic():
                _filter_qs = ElementsFilter.filter(request, self.queryset, kwargs['guide_id'])
                if ElementsActions.check_element_exist(_filter_qs,
                                                       request.GET['code'],
                                                       request.GET['value']):
                    return ResponsesClass.ok_response_no_data()
                else:
                    return ResponsesClass.response_object_not_found()
        except BaseException:
            return ResponsesClass.bad_request_response(
                ErrorHandling.get_traceback()
            )
