from django.db import models
from dating.models import Profile

# Create your models here.


class Message(models.Model):
    s = models.ForeignKey(Profile, on_delete=models.CASCADE)
    message = models.TextField()

class Notification(models.Model):
    message = models.TextField()
