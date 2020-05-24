from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from app.api.v1.urls import urlpatterns as api_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    url('api-auth/', include('rest_framework.urls')),
    url('auth/', include('djoser.urls')),
    url('auth/', include('djoser.urls.authtoken')),
    path('api/v1/', include(api_urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
