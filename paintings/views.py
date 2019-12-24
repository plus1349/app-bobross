from django.shortcuts import get_object_or_404

from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response

from .models import Category, Painting
from .serializers import CategoryListSerializer, PaintingListSerializer, PaintingRetrieveSerializer


class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.filter(enabled=True)
    serializer_class = CategoryListSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response({'results': serializer.data})


class PaintingListAPIView(ListAPIView):
    queryset = Painting.objects.filter(enabled=True)
    serializer_class = PaintingListSerializer

    def get_object(self):
        return get_object_or_404(Category, id=self.kwargs['category'])

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(category=self.get_object())

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response({'results': serializer.data})


class PaintingRetrieveAPIView(RetrieveAPIView):
    serializer_class = PaintingRetrieveSerializer

    def get_object(self):
        return get_object_or_404(Painting, category=self.kwargs['category'], id=self.kwargs['painting'])
