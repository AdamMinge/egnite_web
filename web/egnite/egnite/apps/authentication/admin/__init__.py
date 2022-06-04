from django.contrib import admin
from rest_framework_api_key.models import APIKey

from .organization import OrganizationAdmin
from .organization_api_key import OrganizationApiKeyAdmin

admin.site.unregister(APIKey)

__all__ = [OrganizationAdmin, OrganizationApiKeyAdmin]
