from rest_framework.fields import CharField, EmailField, SerializerMethodField
from rest_framework.serializers import ModelSerializer as BaseModelSerializer, Serializer

from api.serializers import ModelSerializer

from paintings.models import Painting
from users.models import User, UserPainting


class UserAuthSerializer(Serializer):
    deviceId = CharField(max_length=255)

    class Meta:
        fields = ('deviceId',)


class UserLoginSerializer(Serializer):
    email = EmailField(max_length=255)
    password = CharField(max_length=128)

    class Meta:
        fields = ('email', 'password')


# class UserPaintingLayerSerializer(ModelSerializer):
#     image_url = SerializerMethodField()
#
#     class Meta:
#         fields = ('id', 'finish', 'image_url')
#         model = UserPaintingLayer
#
#     def get_image_url(self, instance):
#         return self.context['request'].build_absolute_uri(instance.painting_layer.image.url)


class UserPaintingCreateSerializer(BaseModelSerializer):
    class Meta:
        extra_kwargs = {
            'progress': {'allow_null': False, 'required': True}
        }
        fields = ('complexity', 'progress')
        model = UserPainting

    def create(self, validated_data):
        painting = Painting.objects.get(id=self.context['view'].kwargs['id'])
        user = self.context['request'].user
        return UserPainting.objects.create(painting=painting, user=user, **validated_data)


class UserPaintingSerializer(ModelSerializer):
    archive_url = SerializerMethodField()
    free = SerializerMethodField()
    image_url = SerializerMethodField()
    painting_id = SerializerMethodField()
    progress_url = SerializerMethodField()
    title = SerializerMethodField()

    class Meta:
        fields = ('id', 'painting_id', 'free', 'title', 'complexity', 'archive_url', 'image_url', 'progress_url')
        model = UserPainting

    def get_archive_url(self, instance):
        if instance.painting.archive:
            return self.context['request'].build_absolute_uri(instance.painting.archive.url)

    @staticmethod
    def get_free(instance):
        return instance.painting.free

    def get_image_url(self, instance):
        return self.context['request'].build_absolute_uri(instance.painting.image.url)

    @staticmethod
    def get_painting_id(instance):
        return instance.painting.id

    def get_progress_url(self, instance):
        if instance.progress:
            return self.context['request'].build_absolute_uri(instance.progress.url)

    @staticmethod
    def get_title(instance):
        return instance.painting.title


class UserPaintingUpdateSerializer(BaseModelSerializer):
    class Meta:
        fields = ('complexity', 'progress')
        model = UserPainting

    # def update(self, instance, validated_data):
    #     painting = Painting.objects.get(id=self.context['view'].kwargs['id'])
    #     user = self.context['request'].user
    #     return UserPainting.objects.create(painting=painting, user=user, **validated_data)


class UserProfileSerializer(ModelSerializer):
    class Meta:
        fields = ('id', 'email', 'name', 'phone', 'device_id', 'state')
        model = User


class UserStateUpdateSerializer(BaseModelSerializer):
    class Meta:
        extra_kwargs = {'state': {'required': True, 'allow_null': False, 'allow_blank': False}}
        fields = ('state',)
        model = User
