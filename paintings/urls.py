from django.urls import path

from .views import CategoryListAPIView, PaintingListAPIView, PaintingRetrieveAPIView


urlpatterns = [
    path('categories/', CategoryListAPIView.as_view(), name='category_list'),
    path('paintings/<int:category>/', PaintingListAPIView.as_view(), name='painting_list'),
    path('paintings/<int:category>/<int:painting>/', PaintingRetrieveAPIView.as_view(), name='painting_retrieve'),
]
