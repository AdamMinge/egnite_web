import os

import django
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'egnite.settings')
django.setup()

from .apps.base.middleware import TokenAuthMiddleware
from .apps.chat import routing as chat_routing
from .apps.document import routing as document_routing
from .apps.plugins import routing as plugins_routing

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': AllowedHostsOriginValidator(
        TokenAuthMiddleware(
            URLRouter([*chat_routing.websocket_urlpatterns,
                       *document_routing.websocket_urlpatterns,
                       *plugins_routing.websocket_urlpatterns])
        ),
    )
})
