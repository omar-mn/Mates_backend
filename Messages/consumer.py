from channels.generic.websocket import AsyncWebsocketConsumer
from rest_framework.response import Response


class MessageConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        
        # Get User
        self.user = self.scope["user"]
        if not self.user.is_authenticated:
            await self.close()
            return
        
        #Get Room
        self.room_id = self.scope["url_route"]["kwargs"]["room_id"]
        self.room_group_name = f"room_{self.room_id}"
    
    async def disconnect(self, code):
        pass

    async def receive(self, text_data = None, bytes_data = None):
        print("data recived")