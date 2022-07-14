from rest_framework_api_key.permissions import BaseHasAPIKey

from ..model.organization_api_key import OrganizationAPIKey


class HasOrganizationAPIKey(BaseHasAPIKey):
    model = OrganizationAPIKey
