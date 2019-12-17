from django.urls import path, include
from django.contrib import admin

from django.shortcuts import HttpResponse


def index(request):
    return HttpResponse("INDEX")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
    path('', index),
]
