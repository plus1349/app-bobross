from django.shortcuts import get_object_or_404,render
from django.views.generic import ListView

from rest_framework.generics import CreateAPIView,ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_402_PAYMENT_REQUIRED
from rest_framework.views import APIView

from paintings.models import Painting
from paintings.serializers import PaintingSerializer

from users.models import UserPainting
from users.serializers import UserPaintingCreateSerializer


# class CategoryListAPIView(ListAPIView):
#     queryset = Category.objects.filter(enabled=True)
#     serializer_class = CategoryListSerializer
#
#     def list(self, request, *args, **kwargs):
#         queryset = self.filter_queryset(self.get_queryset())
#         serializer = self.get_serializer(queryset, many=True)
#         return Response({'results': serializer.data})


class PaintingAddAPIView(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserPaintingCreateSerializer

    @property
    def get_object(self):
        return get_object_or_404(Painting, id=self.kwargs['id'])

    def create(self, request, *args, **kwargs):
        painting = self.get_object
        if painting.free:
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid():
                user_painting = serializer.save()
                data = dict(id=user_painting.id, success=True)
                return Response(data=data, status=HTTP_201_CREATED)

            data = dict(success=False, error="Invalid progress file input")
            return Response(data=data, status=HTTP_400_BAD_REQUEST)

        data = dict(success=False, error="Painting is not free")
        return Response(data=data, status=HTTP_402_PAYMENT_REQUIRED)


class PaintingUpdateAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    @property
    def get_object(self):
        return get_object_or_404(Painting, id=self.kwargs['id'])

    def post(self, request, *args, **kwargs):
        painting = self.get_object
        if painting.free:
            if 'progress' in request.FILES:
                user_painting, created = UserPainting.objects.get_or_create(painting=painting, user=request.user)
                status = HTTP_201_CREATED
                if not created:
                    status = HTTP_200_OK

                user_painting.progress = request.FILES['progress']
                user_painting.save(update_fields=('progress',))

                data = dict(success=True)
                return Response(data=data, status=status)

            data = dict(success=False, error="Invalid progress file input")
            return Response(data=data, status=HTTP_400_BAD_REQUEST)

        data = dict(success=False, error="Painting is not free")
        return Response(data=data, status=HTTP_402_PAYMENT_REQUIRED)


# class PaintingCategoryListAPIView(ListAPIView):
#     queryset = Painting.objects.filter(enabled=True)
#     serializer_class = PaintingListSerializer
#
#     def get_object(self):
#         return get_object_or_404(Category, id=self.kwargs['category'])
#
#     def get_queryset(self):
#         queryset = super().get_queryset()
#         return queryset.filter(category=self.get_object())
#
#     def list(self, request, *args, **kwargs):
#         queryset = self.filter_queryset(self.get_queryset())
#         serializer = self.get_serializer(queryset, many=True)
#         return Response({'results': serializer.data})
#
#
class PaintingListAPIView(ListAPIView):
    queryset = Painting.objects.filter(enabled=True)
    serializer_class = PaintingSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response({'results': serializer.data})


class PaintingNewListAPIView(PaintingListAPIView):
    queryset = Painting.objects.filter(enabled=True).order_by('-id')


class PaintingRetrieveAPIView(RetrieveAPIView):
    serializer_class = PaintingSerializer

    def get_object(self):
        return get_object_or_404(Painting, id=self.kwargs['id'])


# class PaintingListView(ListView):
#     queryset = Painting.objects.filter(enabled=True)
#     serializer_class = PaintingSerializer
#     template_name = 'paintings/painting_list.html'
#
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         self.object_list = self.get_queryset()
#
#     def get(self, request, *args, **kwargs):
#         context = self.get_context_data(paintings=self.object_list)
#         return render(request, self.template_name , context)
