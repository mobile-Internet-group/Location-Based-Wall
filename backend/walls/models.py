from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=30, blank=False, null=False)
    password = models.CharField(max_length=30, blank=False, null=False)
    is_manager = models.BooleanField(blank=False,null=False)

class Post(models.Model):
    title = models.CharField(max_length=200)
    content_type = models.TextField()
    text = models.CharField(max_length=200, blank=False, null=False)
    media_url = models.CharField(max_length=200, blank=False, null=False)
    location_x = models.FloatField(max_length=10, blank=False, null=False)
    location_y = models.FloatField(max_length=10, blank=False, null=False)

class Comment(models.Model):
    content_type = models.TextField()
    media_url = models.CharField(max_length=200, blank=False, null=False)
    text = models.CharField(max_length=200, blank=False, null=False)
