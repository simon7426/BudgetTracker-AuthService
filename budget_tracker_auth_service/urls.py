from django.contrib import admin
from django.urls import path, include
from core.views import Alive_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/auth/alive', Alive_view),
    path('api/v1/auth/', include('djoser.urls')),
    path('api/v1/auth/', include('djoser.urls.jwt')),
]
