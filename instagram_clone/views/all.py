from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import redirect, render
from django.urls import reverse

from instagram_clone.forms import PostForm
from instagram_clone.models import Like, Post


@login_required(login_url='users:login', redirect_field_name='next')
def home(request):
    posts = Post.objects.all()
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


@login_required(login_url='users:login', redirect_field_name='next')
def post_edit(request, id):
    post = Post.objects.filter(
        user=request.user,
        pk=id,
    ).first()

    if not post:
        raise Http404()

    form = PostForm(
        data=request.POST or None,
        files=request.FILES or None,
        instance=post,
    )

    if form.is_valid():
        post = form.save(commit=False)
        post.user = request.user
        post.save()

        messages.success(request, 'Save successfully!')
        return redirect(reverse('insta:post_edit', args=(id,)))

    return render(
        request,
        'instagram_clone/pages/post_form.html',
        context={
            'form': form,
            'form_action': reverse('insta:post_edit', args=(id,)),
        }
    )


@login_required(login_url='users:login', redirect_field_name='next')
def post_new(request):
    form = PostForm(
        data=request.POST or None,
        files=request.FILES or None,
    )

    if form.is_valid():
        post: Post = form.save(commit=False)

        post.user = request.user
        post.save()

        messages.success(request, 'Saved successfully')
        return redirect(reverse('insta:post_edit', args=(post.id,)))

    return render(
        request,
        'instagram_clone/pages/post_form.html',
        context={
            'form': form,
            'form_action': reverse('insta:post_new')
        }
    )


@login_required(login_url='users:login', redirect_field_name='next')
def post_like(request):
    if not request.POST:
        return redirect(reverse('insta:home'))

    if request.POST.get('username') != request.user.username:
        return redirect(reverse('insta:home'))

    like = Like.objects.filter(
        user=request.user,
        post=Post.objects.filter(id=request.POST.get('post')).first(),
    )

    if like:
        like.delete()
    else:
        like = Like(
            user=request.user,
            post=Post.objects.filter(id=request.POST.get('post')).first(),
        )
        like.clean()
        like.save()

    post_id = '#post'+request.POST.get('post')

    return redirect(reverse('insta:home')+post_id)
