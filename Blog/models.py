from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from embed_video.fields import EmbedVideoField

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	enrolled = models.ManyToManyField(User,related_name='enrolled',blank=True)
	likers = models.ManyToManyField(User, related_name = 'likers', blank = True)
	location =models.CharField(max_length=100,blank="True",null="True")
	totrating = models.IntegerField(default=0)
	demovid = EmbedVideoField(blank=True,null=True)

	def get_absolute_url(self):
		return reverse('post-detail', kwargs = {'pk':self.pk})

	def rating(self):
		return self.totrating/(5*self.likers.count())



class Comment(models.Model):
	content = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	likes = models.ManyToManyField(User, related_name = 'likes', blank = True)

	def get_absolute_url(self):
		return reverse('post-detail', kwargs = {'pk':self.post.pk})
