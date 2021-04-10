from django.contrib import admin
from .models import Post, Comment,Video

# Register your models here.
admin.site.register(Post)
admin.site.register(Video)
admin.site.register(Comment)
