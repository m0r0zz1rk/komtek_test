from rest_framework import serializers

from apps.guide.models import Guides


class GuidesSerializer(serializers.ModelSerializer):
    """Сериализация модели справочников"""

    id = serializers.SerializerMethodField()

    def get_id(self, obj) -> str:
        """Получение ID объекта справочника"""
        try:
            return str(obj.object_id)
        except Exception:
            return '-'

    get_id.short_description = "ID справочника"

    class Meta:
        model = Guides
        fields = ['id', 'code', 'name']