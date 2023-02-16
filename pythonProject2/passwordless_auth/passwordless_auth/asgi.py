import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import room.routing


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'passwordless_auth.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            room.routing.websocket_urlpatterns
        )
    )
})

