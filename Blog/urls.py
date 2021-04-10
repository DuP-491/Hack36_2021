from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, CommentCreateView

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>/comment/new/', CommentCreateView.as_view(), name='post-comment'),
    path(r'^like/$', views.likepost, name = 'like-post'),
    path('enroll/',views.enroll,name='enroll'),
    path('add_video/<id>/',views.addvideo,name='add_video'),
    path('about/', views.about, name='blog-about'),
    path('play_video/',views.getVideo,name='play-video'),
    path('write_review/<id>/',views.writeReview,name='write-review')
]
