from django.contrib import admin
from django.urls import path, include, re_path

api_urls = [
    path('', include('egnite.apps.documentation.urls')),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('health/', include('health_check.urls')),
    re_path('api/(?P<version>(v1|v2))/', include(api_urls)),
]
