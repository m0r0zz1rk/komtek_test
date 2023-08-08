from datetime import datetime

from django.conf import settings
from django.test import TestCase
from rest_framework.test import RequestsClient

from apps.guide.models import Guides, Versions, Elements


class APITests(TestCase):
    """Класс тестирования API"""

    @classmethod
    def setUpTestData(cls):
        """Создание тестовых данных"""

        # Создание справочников
        refbook1 = Guides.objects.create(
            code=5,
            name='Первый тестовый справочник',
            description=''
        )
        refbook2 = Guides.objects.create(
            code=6,
            name='Второй тестовый справочник',
            description=''
        )

        # Создание версий справочников
        version11 = Versions.objects.create(
            guide_id=refbook1.object_id,
            version='1.1',
            date_start=datetime(2023, 6, 1)
        )
        version12 = Versions.objects.create(
            guide_id=refbook1.object_id,
            version='1.2',
            date_start=datetime(2023, 8, 1)
        )
        Versions.objects.create(
            guide_id=refbook2.object_id,
            version='2.1',
            date_start=datetime(2023, 7, 1)
        )

        # Создание элементов справочников
        Elements.objects.create(
            version_id=version11.object_id,
            code='Ref11-01',
            value='Значение 11-01'
        )
        Elements.objects.create(
            version_id=version12.object_id,
            code='Ref12-01',
            value='Значение 12-01'
        )
        Elements.objects.create(
            version_id=version12.object_id,
            code='Ref21-01',
            value='Значение 21-01'
        )

    def setUp(self):
        """Установка URL для обращения к API, экземпляра класса RequestsClient"""
        self.url = settings.CORS_ALLOWED_ORIGINS[0]
        self.client = RequestsClient()

    def testRefbooks(self):
        """Тестирование API на получение списка справочников"""
        response = self.client.get(f'{self.url}/api/v1/refbooks/')
        assert response.status_code == 200

    def testRefbooksWithDate(self):
        """Тестирование API на получение списка справочников с указанной датой начала действия версий"""
        response = self.client.get(f'{self.url}/api/v1/refbooks?date=2023-06-05')
        assert response.status_code == 200 and len(response.json()['refbooks']) == 1

    def testGuideElements(self):
        """Тестирование API на получение списка элементов справочника"""
        refbook_id = Guides.objects.get(code=5).object_id
        response = self.client.get(f'{self.url}/api/v1/refbooks/{refbook_id}/elements/')
        assert response.status_code == 200 and len(response.json()['elements']) == 3

    def testGuideElementsWithVersion(self):
        """Тестирование API на получение списка элементов справочника с указанной версией"""
        refbook_id = Guides.objects.get(code=5).object_id
        response = self.client.get(f'{self.url}/api/v1/refbooks/{refbook_id}/elements?version=1.2')
        assert response.status_code == 200 and len(response.json()['elements']) == 2

    def testCheckElement(self):
        """Тестирование API на валидацию элементов справочника"""
        refbook_id = Guides.objects.get(code=5).object_id
        response = self.client.get(
            f'{self.url}/api/v1/refbooks/{refbook_id}/check_element?code=Ref12-01&value=Значение 12-01'
        )
        assert response.status_code == 200

    def testCheckElementWithVersion(self):
        """Тестирование API на валидацию элементов справочника"""
        refbook_id = Guides.objects.get(code=5).object_id
        response = self.client.get(
            f'{self.url}/api/v1/refbooks/{refbook_id}/check_element?code=Ref12-01&value=Значение 12-01&version=1.1'
        )
        assert response.status_code == 404
