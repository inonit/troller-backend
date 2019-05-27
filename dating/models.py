from django.db import models
from django.contrib.auth.models import User

# Create your models here.

GENDERS = (
    ('Male', 'male'),
    ('Female', 'female'),
    ('Other', 'other'),
    )

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True)
    date_of_birth = models.DateField(null=True)
    gender = models.CharField(choices=GENDERS, max_length=10)
    image = models.ImageField()
    bio = models.TextField(blank=True)

class Like(models.Model):
    a = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="like_a")
    b = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="like_b")
    liked_p = models.BooleanField(default=False)

class Message(models.Model):
    ## s = sender
    ## r = receiver
    s = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="message_s")
    r = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="message_r")
    message = models.TextField()
