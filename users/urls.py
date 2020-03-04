from django.urls import path

from users.views import (
    user_auth, user_login, user_logout,
    UserPaintingFinishListAPIView, UserPaintingListAPIView, UserPaintingRetrieveAPIView, UserPaintingStartListAPIView,
    UserPaintingUpdateAPIView, UserProfileAPIView, UserStateUpdateAPIView
)


urlpatterns = [
    path('auth/', user_auth, name='user_auth'),
    path('login/', user_login, name='user_login'),
    path('logout/', user_logout, name='user_logout'),
    path('paintings/', UserPaintingListAPIView.as_view(), name='user_painting_list'),
    path('paintings/finish/', UserPaintingFinishListAPIView.as_view(), name='user_painting_finish_list'),
    path('paintings/start/', UserPaintingStartListAPIView.as_view(), name='user_painting_start_list'),
    path('paintings/<int:id>/', UserPaintingRetrieveAPIView.as_view()),
    path('paintings/<int:id>/update/', UserPaintingUpdateAPIView.as_view()),
    path('profile/', UserProfileAPIView.as_view()),
    path('state/update/', UserStateUpdateAPIView.as_view())
]
