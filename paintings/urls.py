from django.urls import path

from paintings.views import CategoryListAPIView, PaintingAddAPIView, PaintingListAPIView, PaintingRetrieveAPIView


urlpatterns = [
    path('categories/', CategoryListAPIView.as_view()),
    path('paintings/<int:category>/', PaintingListAPIView.as_view()),
    path('paintings/<int:category>/<int:painting>/', PaintingRetrieveAPIView.as_view()),
    path('paintings/<int:category>/<int:painting>/add/', PaintingAddAPIView.as_view()),
]
