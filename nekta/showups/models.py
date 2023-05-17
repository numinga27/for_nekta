from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Request(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField(default=datetime.utcnow)
    athour = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='requests')
    status = models.CharField(max_length=20, default='New')


class RequestMessage(models.Model):
    comment = models.TextField()
    date = models.DateTimeField(default=datetime.utcnow)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='messages')
    request = models.ForeignKey(
        Request, on_delete=models.CASCADE, related_name='messages')

