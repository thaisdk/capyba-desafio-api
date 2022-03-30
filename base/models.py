from django.db import models
from django.contrib.auth.models import User

import uuid

# Create your models here.
class Article(models.Model):

    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, unique=True, editable=False)

    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey('Topic', on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    resume = models.CharField(max_length=500, null=True, blank=True)
    body = models.TextField(null=True, blank=True, default='')

    class Meta:
        ordering = ['-updated_at', '-created_at']
    
    
    def __str__(self):
        return self.title


class Message(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['-created_at']


    def __str__(self):
        return self.body[0:20]


class Topic(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
