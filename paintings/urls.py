from django.urls import path

from .views import CategoryListAPIView, PaintingListAPIView, PaintingRetrieveAPIView


urlpatterns = [
    path('', CategoryListAPIView.as_view(), name='category_list'),
    path('<int:category>/', PaintingListAPIView.as_view(), name='painting_list'),
    path('<int:category>/<int:painting>/', PaintingRetrieveAPIView.as_view(), name='painting_retrieve'),
]
