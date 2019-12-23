from django.urls import path

from .views import PaintingListAPIView

urlpatterns = [
    path('', PaintingListAPIView.as_view(), name='painting_list'),
]
