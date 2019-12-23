from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from .models import Category
from .serializers import CategoryListSerializer


class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.filter(enabled=True)
    serializer_class = CategoryListSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response({'results': serializer.data})
