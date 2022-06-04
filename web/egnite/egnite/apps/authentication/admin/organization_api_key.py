from django.contrib import admin
from rest_framework_api_key.admin import APIKeyModelAdmin

from ..model import OrganizationAPIKey


@admin.register(OrganizationAPIKey)
class OrganizationApiKeyAdmin(APIKeyModelAdmin):
    list_display = (*APIKeyModelAdmin.list_display, 'get_organization_name')
    search_fields = [*APIKeyModelAdmin.search_fields, "get_organization_name"]

    @admin.display(ordering='organization__name', description='Organization')
    def get_organization_name(self, obj: OrganizationAPIKey):
        return obj.organization.name
