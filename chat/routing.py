from django.urls import path
from .consumers import EchoConsumer2

websocket_urlpatterns = [
    path('chat/', EchoConsumer2.as_asgi()),
]
