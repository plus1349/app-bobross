from django.urls import path

from paintings.views import PaintingAddAPIView, PaintingListAPIView,PaintingNewListAPIView, PaintingRetrieveAPIView


urlpatterns = [
    path('paintings/', PaintingListAPIView.as_view(), name='painting_list'),
    path('paintings/new/', PaintingNewListAPIView.as_view(), name='painting_new_list'),
    path('paintings/<int:id>/', PaintingRetrieveAPIView.as_view()),
    path('paintings/<int:id>/add/', PaintingAddAPIView.as_view())
]
