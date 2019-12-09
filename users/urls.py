from django.urls import path

from .views import users


urlpatterns = [
    path('', users, name='user_list'),
]
