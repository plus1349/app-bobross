from rest_framework.fields import SerializerMethodField

from api.serializers import ModelSerializer
from paintings.models import Category, PaintingLayer, Painting


class CategoryListSerializer(ModelSerializer):
    class Meta:
        fields = ('id', 'title')
        model = Category


class PaintingLayerListSerializer(ModelSerializer):
    image_url = SerializerMethodField()

    class Meta:
        model = PaintingLayer
        fields = ('id', 'image_url')

    def get_image_url(self, instance):
        return self.context['request'].build_absolute_uri(instance.image.url)


class PaintingListSerializer(ModelSerializer):
    image_url = SerializerMethodField()

    class Meta:
        fields = ('id', 'free', 'title', 'image_url')
        model = Painting

    def get_image_url(self, instance):
        return self.context['request'].build_absolute_uri(instance.image.url)


class PaintingRetrieveSerializer(ModelSerializer):
    image_url = SerializerMethodField()
    layers = PaintingLayerListSerializer(many=True)

    class Meta:
        fields = ('id', 'free', 'title', 'image_url', 'layers')
        model = Painting

    def get_image_url(self, instance):
        return self.context['request'].build_absolute_uri(instance.image.url)
