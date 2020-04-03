from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from django.utils import timezone

from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.generics import GenericAPIView, ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED, HTTP_403_FORBIDDEN, HTTP_404_NOT_FOUND
)

from users.models import User, UserPainting
from users.serializers import (
    UserAuthSerializer, UserLoginSerializer, UserPaintingSerializer, UserPaintingUpdateSerializer,
    UserProfileSerializer, UserStateUpdateSerializer
)


@api_view(('POST',))
def user_login(request):
    serializer = UserLoginSerializer(data=request.data)
    if serializer.is_valid():
        email = serializer.validated_data['email']
        user = User.objects.filter(email=email).first()
        if user is None:
            data = dict(success=False, error="User with given email doesn't exist")
            return Response(data=data, status=HTTP_404_NOT_FOUND)

        if not user.has_usable_password():
            data = dict(success=False, error="User password is not set")
            return Response(data=data, status=HTTP_401_UNAUTHORIZED)

        user = authenticate(email=email, password=serializer.validated_data['password'])
        if user is not None:
            token, c = Token.objects.get_or_create(user=user)
            return Response({"token": token.key})

        data = dict(success=False, error="Invalid password")
        return Response(data=data, status=HTTP_403_FORBIDDEN)

    data = dict(success=False, error="Invalid user login input")
    return Response(data=data, status=HTTP_400_BAD_REQUEST)


@api_view(('POST',))
def user_auth(request):
    serializer = UserAuthSerializer(data=request.data)
    if serializer.is_valid():
        device_id = serializer.validated_data['deviceId']
        user = User.objects.filter(device_id=device_id)
        if user.exists():
            user = user.first()
            token, c = Token.objects.get_or_create(user=user)
            user.last_login = timezone.now()
            user.save(update_fields=('last_login',))
            return Response({"token": token.key})
        user = User.objects.create(email='{device_id}@example.com'.format(device_id=device_id[2:]), device_id=device_id)
        user.set_password(device_id)
        user.save()
        token, c = Token.objects.get_or_create(user=user)
        return Response({"token": token.key}, status=HTTP_201_CREATED)


@api_view(('POST',))
def user_logout(request):
    if not request.user.is_anonymous:
        request.user.auth_token.delete()
        return Response({"success": True})

    data = dict(success=False, error="User is anonymous.")
    return Response(data=data, status=HTTP_401_UNAUTHORIZED)


# class UserCategoryListAPIView(ListAPIView):
#     permission_classes = (IsAuthenticated,)
#     queryset = Category.objects.filter(enabled=True)
#     serializer_class = CategoryListSerializer
#
#     def get_queryset(self):
#         queryset = super().get_queryset()
#         user_paintings = self.request.user.paintings.all()
#         categories_ids = [user_painting.painting.category.id for user_painting in user_paintings.all()]
#         return queryset.filter(id__in=categories_ids)
#
#     def list(self, request, *args, **kwargs):
#         queryset = self.filter_queryset(self.get_queryset())
#         serializer = self.get_serializer(queryset, many=True)
#         return Response({'results': serializer.data})


class UserPaintingFinishListAPIView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = UserPainting.objects.all()
    serializer_class = UserPaintingSerializer

    # def get_queryset(self):
    #     queryset = super().get_queryset().filter(user=self.request.user)
    #     objects = list(filter(lambda obj: obj.finish is True, queryset.all()))
    #     ids = [obj.id for obj in objects]
    #     queryset = queryset.filter(id__in=ids)
    #     return queryset

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user).none()

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response({'results': serializer.data})


# class UserPaintingLayerAPIView(RetrieveAPIView):
#     permission_classes = (IsAuthenticated,)
#     serializer_class = UserPaintingLayerRetrieveSerializer
#
#     def get_object(self):
#         return get_object_or_404(UserPaintingLayer, id=self.kwargs['id'])


# class UserPaintingLayerFinishAPIView(APIView):
#     permission_classes = (IsAuthenticated,)
#
#     def get_object(self):
#         return get_object_or_404(UserPaintingLayer, id=self.kwargs['id'])
#
#     def post(self, request, *args, **kwargs):
#         user_painting_layer = self.get_object()
#         user_painting_layer.finish = True
#         user_painting_layer.save(update_fields=('finish',))
#         return Response({'success': True})


class UserPaintingListAPIView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = UserPainting.objects.all()
    serializer_class = UserPaintingSerializer

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response({'results': serializer.data})


class UserPaintingRetrieveAPIView(RetrieveAPIView):
    serializer_class = UserPaintingSerializer

    def get_object(self):
        return get_object_or_404(UserPainting, id=self.kwargs['id'])


class UserPaintingStartListAPIView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = UserPainting.objects.all()
    serializer_class = UserPaintingSerializer

    # def get_queryset(self):
    #     queryset = super().get_queryset().filter(user=self.request.user)
    #     objects = list(filter(lambda obj: obj.finish is False, queryset.all()))
    #     ids = [obj.id for obj in objects]
    #     queryset = queryset.filter(id__in=ids)
    #     return queryset

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response({'results': serializer.data})


class UserPaintingUpdateAPIView(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserPaintingUpdateSerializer

    @property
    def get_object(self):
        return get_object_or_404(UserPainting, id=self.kwargs['id'], user=self.request.user)

    def post(self, request, *args, **kwargs):
        user_painting = self.get_object
        serializer = self.get_serializer(user_painting, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            data = dict(success=True)
            return Response(data=data, status=HTTP_200_OK)

        data = dict(success=False, error="Invalid user painting update input")
        return Response(data=data, status=HTTP_400_BAD_REQUEST)


class UserProfileAPIView(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserProfileSerializer

    def get_object(self):
        return self.request.user


class UserStateUpdateAPIView(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserStateUpdateSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = request.user
            user.state = serializer.validated_data['state']
            user.save(update_fields=('state',))
            data = dict(success=True)
            return Response(data=data, status=HTTP_200_OK)

        data = dict(success=False, error="Invalid user state update input")
        return Response(data=data, status=HTTP_400_BAD_REQUEST)
