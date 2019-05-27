from rest_framework import generics, mixins
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Profile, Like, Message
from .serializers import ProfileSerializer, LikeSerializer, MessageSerializer, UserSerializer

# Create your views here.


class ProfileCreateView(generics.CreateAPIView):
    serializer_class = ProfileSerializer

class ProfileListView(generics.ListAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()

class UserCreateView(generics.CreateAPIView):
    serializer_class = UserSerializer

class LikeCreateView(generics.CreateAPIView):
    serializer_class = LikeSerializer
    
class LikeListView(generics.ListAPIView):
    serializer_class = LikeSerializer
    queryset = Like.objects.all()

class LikeUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = LikeSerializer
    queryset = Like.objects.all()

class LikeDeleteView(generics.DestroyAPIView):
    serializer_class = LikeSerializer
    queryset = Like.objects.all()

class MessageCreateView(generics.CreateAPIView):
    serializer_class = MessageSerializer
    
class MessageListView(generics.ListAPIView):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()

class MessageUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()

class MessageDeleteView(generics.DestroyAPIView):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()
