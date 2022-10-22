from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import Http404
from django.shortcuts import redirect, render
from django.urls import reverse

from users.forms import LoginForm, RegisterForm


def login_page(request):
    form = LoginForm()
    return render(request, 'users/pages/login.html', {
        'form': form,
        'form_action': reverse('users:login_create'),
    })


def login_create(request):
    if not request.POST:
        raise Http404()

    form = LoginForm(request.POST)

    if form.is_valid():
        authenticated_user = authenticate(
            username=form.cleaned_data.get('username', ''),
            password=form.cleaned_data.get('password', ''),
        )

        if authenticated_user is not None:
            messages.sucess(request, 'Your are logged in.')
            login(request, authenticated_user)
        else:
            messages.error(request, 'Invalid credentials')
    else:
        messages.error(request, 'Invalid username or password')

    return redirect(reverse('insta:home'))


def signup_page(request):
    signup_form_data = request.session.get('signup_form_data', None)
    form = RegisterForm(signup_form_data)
    return render(request, 'users/pages/signup.html', {
        'form': form,
        'form_action': reverse('users:signup_create'),
    })


def signup_create(request):
    if not request.POST:
        raise Http404()

    POST = request.POST
    request.session['signup_form_data'] = POST
    form = RegisterForm(POST)

    if form.is_valid():
        user = form.save(commit=False)
        user.set_password(user.password)
        user.save()
        messages.success(request, 'Your user is created, please log in.')

        del(request.session['signup_form_data'])
        return redirect(reverse('users:login'))

    return redirect('users:signup')
