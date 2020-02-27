from django.urls import path

from paintings.views import (
    CategoryListAPIView, PaintingUpdateAPIView, PaintingCategoryListAPIView, PaintingListAPIView,PaintingNewListAPIView,
    PaintingRetrieveAPIView
)


urlpatterns = [
    path('categories/', CategoryListAPIView.as_view()),
    path('paintings/', PaintingListAPIView.as_view(), name='painting_list'),
    path('paintings/new/', PaintingNewListAPIView.as_view(), name='painting_new_list'),
    # path('paintings/<int:category>/', PaintingCategoryListAPIView.as_view()),
    path('paintings/<int:id>/', PaintingRetrieveAPIView.as_view()),
    path('paintings/<int:id>/update/', PaintingUpdateAPIView.as_view()),
]
