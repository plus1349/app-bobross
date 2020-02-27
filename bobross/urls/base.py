from django.conf import settings
from django.contrib import admin
from django.contrib.staticfiles.urls import static
from django.shortcuts import HttpResponse
from django.urls import path, include
from django.utils.translation import ugettext_lazy as _


# admin.site.index_title = _("App Bob Ross administration")
admin.site.site_header = _("App Bob Ross administration")
admin.site.site_title = _("App Bob Ross administration")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.urls')),

    path('i18n/', include('django.conf.urls.i18n')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
