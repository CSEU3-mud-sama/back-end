from rest_framework import generics
from adventure.models import Room
from .serializers import RoomSerializer, PlayerSerializer

class RoomviewAPI(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer