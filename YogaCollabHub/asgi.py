"""
ASGI config for YogaCollabHub project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter,URLRouter
import interactions.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'YogaCollabHub.settings')

#application = get_asgi_application()

application = ProtocolTypeRouter({
    'http':get_asgi_application(),
    'websocket':AuthMiddlewareStack(
        URLRouter(
            interactions.routing.websocket_urlpatterns
        )
    )
})
