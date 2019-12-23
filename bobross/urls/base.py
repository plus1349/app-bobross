from django.conf import settings
from django.contrib import admin
from django.contrib.staticfiles.urls import static
from django.shortcuts import HttpResponse
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.urls')),

    path('i18n/', include('django.conf.urls.i18n')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
