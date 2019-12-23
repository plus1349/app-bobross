from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response

from .models import Painting
from .serializers import PaintingListSerializer


class PaintingListAPIView(ListAPIView):
    queryset = Painting.objects.filter(enabled=True)
    serializer_class = PaintingListSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response({'results': serializer.data})


# class PaintingRetrieveAPIView(RetrieveAPIView):
#     # queryset = Painting.objects.filter(enabled=True)
#     serializer_class = PaintingRetrieveAPIViewzer
#
#     def list(self, request, *args, **kwargs):
#         queryset = self.filter_queryset(self.get_queryset())
#         serializer = self.get_serializer(queryset, many=True)
#         return Response({'results': serializer.data})
