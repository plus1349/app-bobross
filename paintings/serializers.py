from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from .models import PaintingLayer, Painting

# from categories.serializers import CategoryRetrieveSerializer


class PaintingLayerListSerializer(ModelSerializer):
    image_url = SerializerMethodField()

    class Meta:
        model = PaintingLayer
        fields = ('position', 'image_url')

    def get_image_url(self, instance):
        return self.context['request'].build_absolute_uri(instance.image.url)


class PaintingListSerializer(ModelSerializer):
    # category = CategoryRetrieveSerializer()
    image_url = SerializerMethodField()

    class Meta:
        model = Painting
        fields = ('id', 'free', 'title', 'image_url')

    def get_image_url(self, instance):
        return self.context['request'].build_absolute_uri(instance.image.url)


class PaintingRetrieveSerializer(ModelSerializer):
    # category = CategoryRetrieveSerializer()
    image_url = SerializerMethodField()
    layers = PaintingLayerListSerializer(many=True)

    class Meta:
        model = Painting
        fields = ('id', 'free', 'title', 'image_url', 'layers')

    def get_image_url(self, instance):
        return self.context['request'].build_absolute_uri(instance.image.url)

