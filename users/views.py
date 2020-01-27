from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404

from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED, HTTP_403_FORBIDDEN, HTTP_404_NOT_FOUND
from rest_framework.views import APIView

from paintings.models import Category, Painting
from paintings.serializers import CategoryListSerializer, PaintingListSerializer

from users.models import User, UserPainting, UserPaintingLayer
from users.serializers import (
    UserLoginSerializer, UserPaintingLayerRetrieveSerializer, UserPaintingListSerializer,
    UserPaintingRetrieveSerializer, UserProfileSerializer
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
def user_logout(request):
    if not request.user.is_anonymous:
        request.user.auth_token.delete()
        return Response({"success": True})

    data = dict(success=False, error="User is anonymous.")
    return Response(data=data, status=HTTP_401_UNAUTHORIZED)


class UserCategoryListAPIView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Category.objects.filter(enabled=True)
    serializer_class = CategoryListSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        user_paintings = self.request.user.paintings.all()
        categories_ids = [user_painting.painting.category.id for user_painting in user_paintings.all()]
        return queryset.filter(id__in=categories_ids)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response({'results': serializer.data})


class UserPaintingFinishListAPIView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = UserPainting.objects.all()
    serializer_class = UserPaintingListSerializer

    def get_queryset(self):
        queryset = super().get_queryset().filter(user=self.request.user)
        objects = list(filter(lambda obj: obj.finish is True, queryset.all()))
        ids = [obj.id for obj in objects]
        queryset = queryset.filter(id__in=ids)
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response({'results': serializer.data})


class UserPaintingLayerAPIView(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserPaintingLayerRetrieveSerializer

    def get_object(self):
        return get_object_or_404(UserPaintingLayer, id=self.kwargs['id'])


class UserPaintingLayerFinishAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return get_object_or_404(UserPaintingLayer, id=self.kwargs['id'])

    def post(self, request, *args, **kwargs):
        user_painting_layer = self.get_object()
        user_painting_layer.finish = True
        user_painting_layer.save(update_fields=('finish',))
        return Response({'success': True})


class UserPaintingListAPIView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = UserPainting.objects.all()
    serializer_class = UserPaintingListSerializer

    def get_object(self):
        return get_object_or_404(Category, id=self.kwargs['id'])

    def get_queryset(self):
        queryset = super().get_queryset().filter(painting__category=self.get_object(), user=self.request.user)
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response({'results': serializer.data})


class UserPaintingRetrieveAPIView(RetrieveAPIView):
    serializer_class = UserPaintingRetrieveSerializer

    def get_object(self):
        return get_object_or_404(UserPainting, painting__id=self.kwargs['id'])


class UserPaintingStartListAPIView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = UserPainting.objects.all()
    serializer_class = UserPaintingListSerializer

    def get_queryset(self):
        queryset = super().get_queryset().filter(user=self.request.user)
        objects = list(filter(lambda obj: obj.finish is False, queryset.all()))
        ids = [obj.id for obj in objects]
        queryset = queryset.filter(id__in=ids)
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response({'results': serializer.data})


class UserProfileAPIView(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserProfileSerializer

    def get_object(self):
        return self.request.user
