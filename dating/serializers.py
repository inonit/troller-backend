from rest_framework import serializers
from .models import GENDERS, Profile, Like, Message
from django.contrib.auth.models import User


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = "__all__"

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password")
    def create(self, validated_data):
       password = validated_data.pop("password")
       user = User.objects.create(**validated_data)
       if password:
           user.set_password(password)
           user.save()
       return user
    def update(self, instance, validated_data):
        password = validated_data.pop("password")
        instance.__dict__.update(validated_data)
        if password:
            instance.set_password(password)
        instance.save()
        return instance
