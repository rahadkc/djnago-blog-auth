from django.db import models
from django.contrib.auth.models import User
from django_bleach.models import BleachField   # handles the sanitising


# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = BleachField()
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)
    banner = models.ImageField(blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.title
