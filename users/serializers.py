from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from users.models import User, UserPainting, UserPaintingLayer


class UserPaintingLayerListSerializer(ModelSerializer):
    image_url = SerializerMethodField()

    class Meta:
        fields = ('id', 'finish', 'image_url')
        model = UserPaintingLayer

    def get_image_url(self, instance):
        return self.context['request'].build_absolute_uri(instance.painting_layer.image.url)


class UserPaintingLayerRetrieveSerializer(ModelSerializer):
    image_url = SerializerMethodField()

    class Meta:
        fields = ('id', 'finish', 'image_url')
        model = UserPaintingLayer

    def get_image_url(self, instance):
        return self.context['request'].build_absolute_uri(instance.painting_layer.image.url)


class UserPaintingRetrieveSerializer(ModelSerializer):
    finish = SerializerMethodField()
    free = SerializerMethodField()
    title = SerializerMethodField()
    image_url = SerializerMethodField()
    layers = UserPaintingLayerListSerializer(many=True)

    class Meta:
        fields = ('id', 'free', 'finish', 'title', 'image_url', 'layers')
        model = UserPainting


    @staticmethod
    def get_finish(instance):
        finish = True
        for layer in instance.layers.all():
            if layer.finish is False:
                finish = False
        return finish

    @staticmethod
    def get_free(instance):
        return instance.painting.free

    def get_image_url(self, instance):
        return self.context['request'].build_absolute_uri(instance.painting.image.url)

    @staticmethod
    def get_title(instance):
        return instance.painting.title


class UserProfileSerializer(ModelSerializer):
    class Meta:
        fields = ('id', 'email', 'name')
        model = User