from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50)
    desc = models.TextField(max_length=200)
