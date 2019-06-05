from rest_framework import generics
from .models import Message
from .serializers import MessageSerializer

# Create your views here.


class MessageCreateView(generics.CreateAPIView):
    serializer_class = MessageSerializer

class MessageListView(generics.ListAPIView):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()
