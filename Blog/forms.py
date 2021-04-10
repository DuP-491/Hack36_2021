from django import forms
from django.contrib.auth.models import User
from .models import Video, Review

class VideoCreateForm(forms.ModelForm):
    class Meta:
        model=Video
        fields=['title','description','vid']


class WriteReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'body']
