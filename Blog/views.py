from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post, Comment
from django.template.loader import render_to_string
from django.http import HttpResponseRedirect, JsonResponse


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'Blog/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'Blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        is_enrolled = False
        if (self.object.enrolled.filter(username = self.request.user.username).exists()):
            is_enrolled = True
        else:
            is_enrolled = False
        post = self.object
        # Add in a QuerySet of all the books
        context['comments'] = Comment.objects.filter(post = self.object)
        context['is_enrolled'] = is_enrolled
        context['post']  = post
        return context



class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ['content']
    template_name = 'Blog/comment.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['posty'] = Post.objects.filter(pk = self.kwargs['pk']).first()
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post=Post.objects.filter(pk = self.kwargs['pk']).first()
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return (self.request.user == post.author)


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False



def about(request):
    return render(request, 'Blog/about.html', {'title': 'About'})

#@login_required
def likepost(request):
    post = get_object_or_404(Post, id = request.POST.get('id'))
    is_liked = False
    if (post.likers.filter(username = request.user.username).exists()):
        post.likers.remove(request.user)
        is_liked = False
    else:
        post.likers.add(request.user)
        is_liked = True

    context = {
        'is_liked' : is_liked,
        'post' : post
    }
    html = render_to_string('Blog/like-section.html',context, request = request)
    return JsonResponse({'form':html})
    # else:
    #      return HttpResponseRedirect(post.get_absolute_url())

def enroll(request):
    post = get_object_or_404(Post, id = request.POST.get('id'))
    is_enrolled = False
    if (post.enrolled.filter(username = request.user.username).exists()):
        post.enrolled.remove(request.user)
        is_enrolled = False
    else:
        post.enrolled.add(request.user)
        is_enrolled = True

    context = {
        'is_enrolled' : is_enrolled,
        'post' : post
    }
    html = render_to_string('Blog/enroll.html',context, request = request)
    return JsonResponse({'form':html})