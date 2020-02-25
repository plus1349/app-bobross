from django.shortcuts import get_object_or_404

from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_402_PAYMENT_REQUIRED
from rest_framework.views import APIView

from paintings.models import Category, Painting
from paintings.serializers import CategoryListSerializer, PaintingListSerializer, PaintingRetrieveSerializer

from users.models import UserPainting, UserPaintingLayer


class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.filter(enabled=True)
    serializer_class = CategoryListSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response({'results': serializer.data})


class PaintingAddAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    @property
    def get_object(self):
        return get_object_or_404(Painting, id=self.kwargs['id'])

    def post(self, request, *args, **kwargs):
        painting = self.get_object
        if painting.free:
            if 'progress' in request.FILES:
                user_painting, created = UserPainting.objects.get_or_create(painting=painting, user=request.user)
                if not created:
                    data = dict(success=False, error="User painting already exists")
                    return Response(data=data, status=HTTP_400_BAD_REQUEST)

                user_painting.progress = request.FILES['progress']
                user_painting.save(update_fields=('progress',))

                data = dict(success=True)
                return Response(data=data, status=HTTP_200_OK)

            data = dict(success=False, error="Invalid progress file input")
            return Response(data=data, status=HTTP_400_BAD_REQUEST)

        data = dict(success=False, error="Painting is not free")
        return Response(data=data, status=HTTP_402_PAYMENT_REQUIRED)


        # painting = self.get_object
        # if painting.free:
        #     user_painting, created = UserPainting.objects.get_or_create(user=self.request.user, painting=painting)
        #     if not created:
        #         data = dict(success=False, error="User painting already exists")
        #         return Response(data=data, status=HTTP_400_BAD_REQUEST)
        #
        #     for painting_layer in painting.layers.all():
        #         user_painting_layer, created = UserPaintingLayer.objects.get_or_create(
        #             user_painting=user_painting,
        #             painting_layer=painting_layer
        #         )
        #         if not created:
        #             data = dict(success=False, error="User painting layer already exists")
        #             return Response(data=data, status=HTTP_400_BAD_REQUEST)
        #
        #     data = dict(success=True)
        #     return Response(data=data, status=HTTP_200_OK)
        #
        # data = dict(success=False, error="Painting is not free")
        # return Response(data=data, status=HTTP_402_PAYMENT_REQUIRED)


class PaintingCategoryListAPIView(ListAPIView):
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


class PaintingListAPIView(ListAPIView):
    queryset = Painting.objects.filter(enabled=True)
    serializer_class = PaintingListSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response({'results': serializer.data})


class PaintingNewListAPIView(PaintingListAPIView):
    queryset = Painting.objects.filter(enabled=True).order_by('-id')


class PaintingRetrieveAPIView(RetrieveAPIView):
    serializer_class = PaintingRetrieveSerializer

    def get_object(self):
        return get_object_or_404(Painting, id=self.kwargs['id'])
