from rest_framework import serializers

from apps.guide.models import Elements


class ElementsSerializer(serializers.ModelSerializer):
    """Сериализация модели элементов справочника"""
    class Meta:
        model = Elements
        fields = ['code', 'value']