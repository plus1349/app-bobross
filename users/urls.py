from django.urls import path

from users.views import (
    user_auth, user_login, user_logout,
    UserCategoryListAPIView, UserPaintingFinishListAPIView, UserPaintingLayerAPIView, UserPaintingLayerFinishAPIView,
    UserPaintingListAPIView, UserPaintingRetrieveAPIView, UserPaintingStartListAPIView, UserProfileAPIView
)


urlpatterns = [
    path('auth/', user_auth, name='user_auth'),
    path('login/', user_login, name='user_login'),
    path('logout/', user_logout, name='user_logout'),
    path('categories/', UserCategoryListAPIView.as_view(), name='user_category_list'),
    path('paintings/', UserPaintingListAPIView.as_view(), name='user_painting_list'),
    path('paintings/finish/', UserPaintingFinishListAPIView.as_view(), name='user_painting_finish_list'),
    path('paintings/start/', UserPaintingStartListAPIView.as_view(), name='user_painting_start_list'),
    # path('paintings/<int:category>/', UserPaintingListAPIView.as_view()),
    path('paintings/<int:id>/', UserPaintingRetrieveAPIView.as_view()),
    # path('paintings/<int:category>/<int:painting>/<int:layer>/', UserPaintingLayerAPIView.as_view()),
    path('paintings/layers/<int:id>/', UserPaintingLayerAPIView.as_view()),
    path('paintings/layers/<int:id>/finish/', UserPaintingLayerFinishAPIView.as_view()),
    path('profile/', UserProfileAPIView.as_view()),
]
