from rest_framework.permissions import IsAuthenticated

from .api_key_access_policy import APIKeyAccessPolicy


class AuthenticatedAccessPolicy(APIKeyAccessPolicy):
    def __init__(self):
        super().__init__()
        self.is_authenticated = IsAuthenticated()

    def has_permission(self, request, view):
        return self.is_authenticated.has_permission(request, view) and \
               APIKeyAccessPolicy.has_permission(self, request, view)

    def has_object_permission(self, request, view, obj):
        return self.is_authenticated.has_object_permission(request, view, obj) and \
               APIKeyAccessPolicy.has_object_permission(self, request, view, obj)
