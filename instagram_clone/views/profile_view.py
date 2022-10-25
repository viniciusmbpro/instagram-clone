from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from instagram_clone.models import Post, Like
from instagram_clone.forms import ProfileForm


@login_required(login_url='users:login', redirect_field_name='next')
def profile(request):
    posts = Post.objects.filter(user=request.user)
    num_posts = posts.count()
    dados: list[str] = []
    for post in posts:
        num_likes = Like.objects.filter(
            post=post,
        ).count()
        dados.append((
            post,
            num_likes,
        ))
    return render(request, 'instagram_clone/pages/profile.html', {
        'posts': dados,
        'num_posts': num_posts,
    })


@login_required(login_url='users:login', redirect_field_name='next')
def profile_edit(request):
    form = ProfileForm()
    return render(request, 'instagram_clone/pages/profile_edit.html', {
        'form': form,
    })
