from django.urls import path

from users.views import (
    UserCategoryListAPIView, UserPaintingLayerAPIView, UserPaintingLayerFinishAPIView, UserPaintingListAPIView,
    UserPaintingRetrieveAPIView, UserProfileAPIView
)


urlpatterns = [
    path('users/', UserCategoryListAPIView.as_view()),
    path('users/paintings/<int:category>/', UserPaintingListAPIView.as_view()),
    path('users/paintings/<int:category>/<int:painting>/', UserPaintingRetrieveAPIView.as_view()),
    path('users/paintings/<int:category>/<int:painting>/<int:layer>/', UserPaintingLayerAPIView.as_view()),
    path('users/paintings/<int:category>/<int:painting>/<int:layer>/finish/', UserPaintingLayerFinishAPIView.as_view()),
    path('users/profile/', UserProfileAPIView.as_view()),
]
