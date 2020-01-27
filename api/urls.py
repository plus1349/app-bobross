from django.urls import include, path


urlpatterns = [
    path('', include('paintings.urls')),
    path('users/', include('users.urls')),
]
