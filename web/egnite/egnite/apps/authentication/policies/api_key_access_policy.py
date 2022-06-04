from rest_access_policy import AccessPolicy
from rest_framework_api_key.permissions import HasAPIKey


class APIKeyAccessPolicy(AccessPolicy):
    def __init__(self):
        super().__init__()
        self.has_organization_api_key = HasAPIKey()

    def has_permission(self, request, view):
        return self.has_organization_api_key.has_permission(request, view) and \
               AccessPolicy.has_permission(self, request, view)

    def has_object_permission(self, request, view, obj):
        return self.has_organization_api_key.has_object_permission(request, view, obj) and \
               AccessPolicy.has_object_permission(self, request, view, obj)
