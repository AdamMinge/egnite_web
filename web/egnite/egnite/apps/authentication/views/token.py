from drf_yasg.utils import swagger_auto_schema
from rest_access_policy import AccessViewSetMixin
from rest_framework import status
from rest_framework_simplejwt.views import (
    TokenBlacklistView,
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from ..serializers import (TokenObtainPairResponseSerializer, TokenRefreshResponseSerializer,
                           TokenVerifyResponseSerializer, TokenBlacklistResponseSerializer)
from ..policies import APIKeyAccessPolicy


# noinspection DuplicatedCode
class DecoratedTokenObtainPairView(AccessViewSetMixin, TokenObtainPairView):
    access_policy = APIKeyAccessPolicy
    permission_classes = []

    # noinspection PyTypeChecker
    @swagger_auto_schema(
        responses={
            status.HTTP_200_OK: TokenObtainPairResponseSerializer,
        }
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class DecoratedTokenRefreshView(AccessViewSetMixin, TokenRefreshView):
    access_policy = APIKeyAccessPolicy
    permission_classes = []

    # noinspection PyTypeChecker
    @swagger_auto_schema(
        responses={
            status.HTTP_200_OK: TokenRefreshResponseSerializer,
        }
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


# noinspection DuplicatedCode
class DecoratedTokenVerifyView(AccessViewSetMixin, TokenVerifyView):
    access_policy = APIKeyAccessPolicy
    permission_classes = []

    # noinspection PyTypeChecker
    @swagger_auto_schema(
        responses={
            status.HTTP_200_OK: TokenVerifyResponseSerializer,
        }
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class DecoratedTokenBlacklistView(AccessViewSetMixin, TokenBlacklistView):
    access_policy = APIKeyAccessPolicy
    permission_classes = []

    # noinspection PyTypeChecker
    @swagger_auto_schema(
        responses={
            status.HTTP_200_OK: TokenBlacklistResponseSerializer,
        }
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
