from django.conf import settings
from django.contrib import admin
from django.contrib.staticfiles.urls import static
from django.shortcuts import redirect, render_to_response
from django.urls import include, path, re_path
from django.utils.translation import ugettext_lazy as _


admin.site.site_header = _("App Bob Ross administration")
admin.site.site_title = _("App Bob Ross administration")


def index(request):
    return render_to_response('index.html')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
    path('index/', index),

    re_path(r'^', include('cms.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
