from django.contrib.auth.models import AnonymousUser
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import AccessToken, TokenError
from channels.db import database_sync_to_async
from channels.middleware import BaseMiddleware

User = get_user_model()


@database_sync_to_async
def get_user(user_id):
    try:
        return User.object.get(id=user_id)
    except User.DoesNotExist:
        return AnonymousUser()


class TokenAuthMiddleware(BaseMiddleware):
    def __init__(self, inner):
        super().__init__(inner)

    async def __call__(self, scope, receive, send):
        try:
            token = dict(scope['headers'])[b'sec-websocket-protocol'].decode('utf-8')
        except ValueError:
            token = None

        try:
            access_token = AccessToken(token)
            scope['user'] = await get_user(access_token['user_id'])
        except TokenError:
            scope['user'] = AnonymousUser()

        return await super().__call__(scope, receive, send)
