from django.contrib import admin
from rest_framework_api_key.admin import APIKeyModelAdmin

from ..model import OrganizationAPIKey


@admin.register(OrganizationAPIKey)
class OrganizationApiKeyAdmin(APIKeyModelAdmin):
    list_display = (*APIKeyModelAdmin.list_display, 'organization__name')
    search_fields = [*APIKeyModelAdmin.search_fields, "organization__name"]
