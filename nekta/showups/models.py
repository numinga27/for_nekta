from django.db import models
from django.contrib.auth.models import AbstractUser


STATUS_CHOICES = (
    ('new', 'New'),
    ('old', 'Old'),
    ('in_process', 'In process'),
)

class User(AbstractUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    requests = models.ManyToManyField('Request', through='RequestMembership', related_name='members')
    messages = models.ManyToManyField('RequestMessage', through='MessageMembership', related_name='users', blank=True)

    def __str__(self):
        return self.username

class Request(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

class RequestMessage(models.Model):
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    message_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='message_user')
    message_request = models.ForeignKey(Request, on_delete=models.CASCADE, related_name='message_request')

class RequestMembership(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    request = models.ForeignKey(Request, on_delete=models.CASCADE)
    date_joined = models.DateTimeField(auto_now_add=True)

class MessageMembership(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.ForeignKey(RequestMessage, on_delete=models.CASCADE)
    date_joined = models.DateTimeField(auto_now_add=True)

