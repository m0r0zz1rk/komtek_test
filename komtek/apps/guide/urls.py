from django.urls import path

from apps.guide.api.elements_viewset import ElementsViewSet
from apps.guide.api.guides_viewset import GuidesViewSet

urlpatterns = [
    path('refbooks/', GuidesViewSet.as_view({'get': 'get_guides_list'})),
    path('refbooks/<uuid:guide_id>/elements/', ElementsViewSet.as_view({'get': 'get_elements_list'})),
    path('refbooks/<uuid:guide_id>/check_element/', ElementsViewSet.as_view({'get': 'check_element_exist'}))
]