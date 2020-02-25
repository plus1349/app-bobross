from rest_framework.fields import FileField, SerializerMethodField
from rest_framework.serializers import ModelSerializer as BaseModelSerializer

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
    archive_url = SerializerMethodField()

    class Meta:
        fields = ('id', 'free', 'title', 'layers_count', 'size_name', 'archive_url', 'image_url')
        model = Painting

    def get_archive_url(self, instance):
        if instance.archive:
            return self.context['request'].build_absolute_uri(instance.archive.url)

    def get_image_url(self, instance):
        if instance.image:
            return self.context['request'].build_absolute_uri(instance.image.url)


class PaintingRetrieveSerializer(ModelSerializer):
    archive_url = SerializerMethodField()
    image_url = SerializerMethodField()
    # layers = PaintingLayerListSerializer(many=True)

    class Meta:
        # fields = ('id', 'free', 'title', 'image_url', 'layers')
        fields = ('id', 'free', 'title', 'layers_count', 'size_name', 'archive_url', 'image_url')
        model = Painting

    def get_archive_url(self, instance):
        if instance.archive:
            return self.context['request'].build_absolute_uri(instance.archive.url)

    def get_image_url(self, instance):
        if instance.image:
            return self.context['request'].build_absolute_uri(instance.image.url)
