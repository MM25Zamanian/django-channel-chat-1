from channels.generic.websocket import AsyncJsonWebsocketConsumer
from asgiref.sync import async_to_sync


class EchoConsumer2(AsyncJsonWebsocketConsumer):
    async def connect(self):
        self.user = self.scope["user"]
        if self.user.is_authenticated:
            self.room_name = 'global'
            self.room_group_name = 'chat_global'

            await self.channel_layer.group_add(self.room_group_name,
                                               self.channel_name)
            await self.accept()
        else:
            await self.close()

    async def receive(self, text_data):
        await self.channel_layer.group_send(self.room_group_name, {
            'type': 'chat_message',
            'message': text_data,
            'user': self.user,
        })

    async def chat_message(self, event):
        message = f"{event['user']}:{event['message']}"

        # Send message to WebSocket
        await self.send(text_data=message)
