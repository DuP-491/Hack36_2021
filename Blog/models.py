from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from embed_video.fields import EmbedVideoField
from taggit.managers import TaggableManager

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=100)
	image = models.ImageField(default='cdefault.jpg',upload_to='courses')
	content = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	enrolled = models.ManyToManyField(User,related_name='enrolled',blank=True)
	likers = models.ManyToManyField(User, related_name = 'likers', blank = True)
	price = models.IntegerField(default=0)
	location =models.CharField(max_length=100,blank="True",null="True")
	totrating = models.IntegerField(default=0)
	demovid = EmbedVideoField(blank=True,null=True)
	tags = TaggableManager()

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

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'videos/course_{0}/{1}'.format(instance.course.id, filename)

def usert_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'thumbnails/course_{0}/{1}'.format(instance.course.id, filename)

class Video(models.Model):
	course = models.ForeignKey(Post,on_delete=models.CASCADE)
	author = models.ForeignKey(User,on_delete=models.CASCADE)
	title = models.CharField(max_length=128)
	description = models.TextField()
	vid = models.FileField(upload_to=user_directory_path)
	thumbnail = models.ImageField(upload_to=usert_directory_path,default='default.jpg')


class Review(models.Model):
	course = models.ForeignKey(Post,on_delete=models.CASCADE)
	author = models.ForeignKey(User,on_delete=models.CASCADE)
	rating = models.IntegerField(default=0)
	body = models.TextField()
