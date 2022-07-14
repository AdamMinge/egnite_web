from rest_access_policy import AccessPolicy

from ..permissions import HasOrganizationAPIKey


class APIKeyAccessPolicy(AccessPolicy):
    statements = [
        {
            "action": ["*"],
            "principal": ["*"],
            "effect": "allow",
        },
    ]

    def __init__(self):
        super().__init__()
        self.has_organization_api_key = HasOrganizationAPIKey()

    def has_permission(self, request, view):
        return self.has_organization_api_key.has_permission(request, view) and \
               AccessPolicy.has_permission(self, request, view)

    def has_object_permission(self, request, view, obj):
        return self.has_organization_api_key.has_object_permission(request, view, obj) and \
               AccessPolicy.has_object_permission(self, request, view, obj)
