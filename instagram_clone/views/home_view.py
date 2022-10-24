from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from instagram_clone.models import Like, Post


@login_required(login_url='users:login', redirect_field_name='next')
def home(request):
    posts = Post.objects.all().order_by('-id')
    dados: list[str] = []
    for post in posts:
        liked = Like.objects.filter(
            user=request.user,
            post=post,
        ).first()

        likes = Like.objects.filter(
            post=post,
        ).count()
        dados.append((
            post,
            {
                'liked': liked,
                'n_likes': likes,
            },
        ))

    return render(request, 'instagram_clone/pages/home.html', {
        'range': range(10),
        'posts': dados,
    })
