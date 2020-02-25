from rest_framework.fields import CharField, EmailField, SerializerMethodField
from rest_framework.serializers import Serializer

from api.serializers import ModelSerializer
from users.models import User, UserPainting, UserPaintingLayer


class UserAuthSerializer(Serializer):
    deviceId = CharField(max_length=255)

    class Meta:
        fields = ('deviceId',)


class UserLoginSerializer(Serializer):
    email = EmailField(max_length=255)
    password = CharField(max_length=128)

    class Meta:
        fields = ('email', 'password')


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


class UserPaintingListSerializer(ModelSerializer):
    archive_url = SerializerMethodField()
    # finish = SerializerMethodField()
    free = SerializerMethodField()
    image_url = SerializerMethodField()
    layers_count = SerializerMethodField()
    progress_url = SerializerMethodField()
    size_name = SerializerMethodField()
    title = SerializerMethodField()

    class Meta:
        fields = ('id', 'free', 'title', 'layers_count', 'size_name', 'archive_url', 'image_url', 'progress_url')
        model = UserPainting

    def get_archive_url(self, instance):
        if instance.painting.archive:
            return self.context['request'].build_absolute_uri(instance.painting.archive.url)

    @staticmethod
    def get_free(instance):
        return instance.painting.free

    # @staticmethod
    # def get_finish(instance):
    #     finish = True
    #     for layer in instance.layers.all():
    #         if layer.finish is False:
    #             finish = False
    #     return finish

    def get_image_url(self, instance):
        if instance.painting.image:
            return self.context['request'].build_absolute_uri(instance.painting.image.url)

    @staticmethod
    def get_layers_count(instance):
        return instance.painting.layers_count

    def get_progress_url(self, instance):
        if instance.progress:
            return self.context['request'].build_absolute_uri(instance.progress.url)

    @staticmethod
    def get_size_name(instance):
        return instance.painting.size_name

    @staticmethod
    def get_title(instance):
        return instance.painting.title


class UserPaintingRetrieveSerializer(ModelSerializer):
    archive_url = SerializerMethodField()
    # finish = SerializerMethodField()
    free = SerializerMethodField()
    image_url = SerializerMethodField()
    layers_count = SerializerMethodField()
    progress_url = SerializerMethodField()
    size_name = SerializerMethodField()
    # layers = UserPaintingLayerListSerializer(many=True)
    title = SerializerMethodField()

    class Meta:
        fields = ('id', 'free', 'title', 'layers_count', 'size_name', 'archive_url', 'image_url', 'progress_url')
        model = UserPainting

    def get_archive_url(self, instance):
        if instance.painting.archive:
            return self.context['request'].build_absolute_uri(instance.painting.archive.url)

    # @staticmethod
    # def get_finish(instance):
    #     finish = True
    #     for layer in instance.layers.all():
    #         if layer.finish is False:
    #             finish = False
    #     return finish

    @staticmethod
    def get_free(instance):
        return instance.painting.free

    def get_image_url(self, instance):
        return self.context['request'].build_absolute_uri(instance.painting.image.url)

    @staticmethod
    def get_layers_count(instance):
        return instance.painting.layers_count

    def get_progress_url(self, instance):
        if instance.progress:
            return self.context['request'].build_absolute_uri(instance.progress.url)

    @staticmethod
    def get_size_name(instance):
        return instance.painting.size_name

    @staticmethod
    def get_title(instance):
        return instance.painting.title


class UserProfileSerializer(ModelSerializer):
    state_url = SerializerMethodField()

    class Meta:
        fields = ('id', 'email', 'name', 'phone', 'device_id', 'state_url')
        model = User

    def get_state_url(self, instance):
        if instance.state:
            return self.context['request'].build_absolute_uri(instance.state.url)
