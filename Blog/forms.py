from django import forms
from django.contrib.auth.models import User
from .models import Video, Review

class VideoCreateForm(forms.ModelForm):
    class Meta:
        model=Video
        fields=['title','description','vid','thumbnail']


class WriteReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['body']
