from django.urls import path
from django.contrib import admin

from django.shortcuts import HttpResponse


def index(request):
    return HttpResponse("INDEX")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
]
