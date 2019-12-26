from django.urls import path

from users.views import (
    user_login, user_logout,
    UserCategoryListAPIView, UserPaintingListAPIView, UserPaintingRetrieveAPIView, UserProfileAPIView
)


urlpatterns = [
    path('login/', user_login, name='user_login'),
    path('logout/', user_logout, name='user_logout'),
    path('categories/', UserCategoryListAPIView.as_view(), name='user_category_list'),
    path('paintings/<int:category>/', UserPaintingListAPIView.as_view(), name='user_painting_list'),
    path('paintings/<int:category>/<int:painting>/', UserPaintingRetrieveAPIView.as_view(), name='user_painting_retrieve'),
    path('profile/', UserProfileAPIView.as_view(), name='user_profile'),
]
