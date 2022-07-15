from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
    
class Cyberspace(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(default='cyber_def.jpg', upload_to='cyberspace')
    credit = models.CharField(max_length=100, default='Anonymous')
    
    def __str__(self):
        return self.title
     
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        img = Image.open(self.image.path)
        
        if img.height > 300 or img.width > 300:
            output_size = (567, 400)
            img.thumbnail(output_size)
            img.save(self.image.path)
            
class Link(models.Model):
    title = models.CharField(max_length=100, default=False)
    link = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title
    
class Service(models.Model):
    title = models.CharField(max_length=100, default='Cyber')
    content = models.TextField(max_length=1000)
    image = models.ImageField(default='cyber_def.jpg', upload_to='service')
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        img = Image.open(self.image.path)
        
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
            
class Brands_list(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(default='default.jpg', upload_to='brand_images')
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        img = Image.open(self.image.path)
        
        if img.height > 300 or img.width > 300:
            output_size = (256, 184)
            img.thumbnail(output_size)
            img.save(self.image.path)
            
class Org_info(models.Model):
    org_name = models.CharField(max_length=100)
    org_mail = models.CharField(max_length=100)
    org_mobile = models.CharField(max_length=100)
    org_address = models.CharField(max_length=500)
    image = models.ImageField(default='default.jpg', upload_to='org_info_image')
    
    def __str__(self):
        return self.org_name