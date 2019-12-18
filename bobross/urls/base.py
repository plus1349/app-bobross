from django.conf import settings
from django.contrib import admin
from django.contrib.staticfiles.urls import static
from django.shortcuts import HttpResponse
from django.urls import path, include


def index(request):
    return HttpResponse("INDEX")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
    path('', index),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
