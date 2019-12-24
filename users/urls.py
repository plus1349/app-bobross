from django.urls import path

from .views import UserCategoryListAPIView, UserPaintingListAPIView, UserPaintingRetrieveAPIView, UserProfileAPIView


urlpatterns = [
    path('users/', UserCategoryListAPIView.as_view(), name='user_category_list'),
    path('users/<int:category>/', UserPaintingListAPIView.as_view(), name='user_painting_list'),
    path('users/<int:category>/<int:painting>/', UserPaintingRetrieveAPIView.as_view(), name='user_painting_retrieve'),
    path('users/profile/', UserProfileAPIView.as_view(), name='user_profile'),
]
