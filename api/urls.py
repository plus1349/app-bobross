from django.urls import include, path


urlpatterns = [
    path('', include('paintings.urls')),
    path('', include('users.urls')),
]
