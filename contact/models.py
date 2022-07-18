from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Message(models.Model):
    full_name = models.CharField(max_length=200, default="Your name")
    email_address = models.EmailField(max_length=200, default="Email address")
    subject = models.CharField(max_length=300, default="Subject")
    message = models.TextField()
    
    def __str__(self):
        return self.message
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)