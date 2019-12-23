from rest_framework.serializers import ModelSerializer

from .models import Category


class CategoryListSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title')


class CategoryRetrieveSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title')
