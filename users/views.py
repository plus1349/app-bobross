from django.shortcuts import get_object_or_404

from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from paintings.models import Category, Painting
from users.models import UserPainting

from paintings.serializers import CategoryListSerializer, PaintingListSerializer, PaintingRetrieveSerializer
from users.serializers import UserPaintingRetrieveSerializer, UserProfileSerializer


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


class UserPaintingListAPIView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = UserPainting.objects.all()
    serializer_class = PaintingListSerializer

    def get_object(self):
        return get_object_or_404(Category, id=self.kwargs['category'])

    def get_queryset(self):
        user_paintings =  super().get_queryset().filter(user=self.request.user)
        paintings_ids = [user_painting.painting.id for user_painting in user_paintings.all()]
        paintings = Painting.objects.filter(category=self.get_object(), id__in=paintings_ids)
        return paintings

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response({'results': serializer.data})


class UserPaintingRetrieveAPIView(RetrieveAPIView):
    serializer_class = UserPaintingRetrieveSerializer

    def get_object(self):
        obj =  get_object_or_404(UserPainting, painting__category=self.kwargs['category'], painting__id=self.kwargs['painting'])
        return obj


class UserProfileAPIView(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserProfileSerializer

    def get_object(self):
        return self.request.user
