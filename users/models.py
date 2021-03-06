from django import forms
from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from Blog.models import Post


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    city = models.CharField(max_length=100,null=True,blank=True)
    followers=models.ManyToManyField(User,related_name='followers')
    followings=models.ManyToManyField(User,related_name='followings')
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username}'
