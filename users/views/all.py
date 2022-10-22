from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
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
            messages.success(request, 'Your are logged in.')
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


@login_required(login_url='users:login', redirect_field_name='next')
def logout_trigger(request):
    if not request.POST:
        messages.error(request, 'Invalid logout request')
        return redirect(reverse('users:login'))

    if request.POST.get('username') != request.user.username:
        messages.error(request, 'Invalid logout user')
        return redirect(reverse('users:login'))

    messages.success(request, 'Logged out successfully')
    logout(request)
    return redirect(reverse('users:login'))
