from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import redirect, render
from django.urls import reverse

from instagram_clone.forms import ProfileForm, UserForm
from instagram_clone.models import Like, Post, Profile


@login_required(login_url='users:login', redirect_field_name='next')
def profile(request, username):
    posts = Post.objects.filter(user__username=username)
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

    profile = Profile.objects.filter(user__username=username).first()
    return render(request, 'instagram_clone/pages/profile.html', {
        'profile': profile,
        'posts': dados,
        'num_posts': num_posts,
    })


@login_required(login_url='users:login', redirect_field_name='next')
def profile_edit(request, id):
    profile = Profile.objects.filter(
        user=request.user,
    ).first()

    if request.user.id != id:
        raise Http404()

    user_form = UserForm(
        data=request.POST or None,
        instance=request.user,
    )
    profile_form = ProfileForm(
        data=request.POST or None,
        files=request.FILES or None,
        instance=profile,
    )

    if user_form.is_valid() & profile_form.is_valid():
        user = user_form.save(commit=False)
        user.save()

        profile = profile_form.save(commit=False)
        profile.save()

        messages.success(request, 'Save successfully!')
        return redirect(reverse('insta:profile_edit', args=(id,)))

    return render(
        request,
        'instagram_clone/pages/profile_edit.html',
        context={
            'user_form': user_form,
            'profile_form': profile_form,
            'form_action': reverse('insta:profile_edit', args=(id,)),
        }
    )
