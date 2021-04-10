from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, ListView
from .models import Profile
from Blog.models import Post
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.http import HttpResponseRedirect, JsonResponse


# Create your views here.
def register(request):
    if (request.method == 'POST'):
        form = UserRegisterForm(request.POST)
        if (form.is_valid()):
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request, user):
    user = User.objects.filter(username=user).first()
    print(user)
    if user == request.user:
        if (request.method == 'POST'):
            u_form = UserUpdateForm(request.POST, instance=user)
            p_form = ProfileUpdateForm(request.POST, request.FILES, instance=user.profile)

            if (u_form.is_valid() and p_form.is_valid()):
                u_form.save()
                p_form.save()
                messages.success(request, 'Account has been updated.')
                return redirect('profile')
        else:
            u_form = UserUpdateForm(instance=request.user)
            p_form = ProfileUpdateForm(instance=request.user.profile)
            followers=user.profile.followers.all()
            followings=user.profile.followings.all()
        context = {
            'uform': u_form,
            'pform': p_form,
            'followers': followers,
            'followings': followings,
        }
        return render(request, 'users/profile.html', context)
    else:
        pro=Profile.objects.filter(user=user).first()
        followers = user.profile.followers.all()
        followings = user.profile.followings.all()
        context = {}
        context['posts'] = Post.objects.filter(author=user)
        context['object'] = Profile.objects.filter(user=user).first()
        context['followers'] =user.profile.followers.all()
        context['following'] = user.profile.followings.all()
        if pro.followers.filter(username=request.user).exists():
            context['is_followed']=True
        else:
            context['is_followed']=False

        return render(request, 'users/profile_other.html', context)


def follow(request):
    userd = request.POST.get('username')
    userd=User.objects.get(username=userd)
    user = Profile.objects.filter(user=userd).first()
    is_followed = False
    if (user.followers.filter(username=request.user).exists()):
        user.followers.remove(request.user)
        request.user.profile.followings.remove(userd)
        is_followed = False
    else:
        user.followers.add(request.user)
        request.user.profile.followings.add(userd)
        is_followed = True


    context = {
        'is_followed': is_followed,
        'object': user
    }
    html = render_to_string('users/follow.html', context, request=request)
    return JsonResponse({'form': html})


class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'users/profile_other.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['posts'] = Post.objects.filter(author__profile=self.object)
        return context
