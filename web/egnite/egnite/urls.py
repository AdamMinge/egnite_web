from django.contrib import admin
from django.urls import path, include, re_path

api_urls = [
    path('', include('egnite.apps.authentication.urls')),
    path('', include('egnite.apps.documentation.urls')),
    path('', include('egnite.apps.chat.urls')),
    path('', include('egnite.apps.plugin.urls')),
    path('', include('egnite.apps.document.urls')),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('health/', include('health_check.urls')),
    re_path('api/(?P<version>(v1|v2))/', include(api_urls)),
]
