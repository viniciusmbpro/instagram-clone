from django.contrib import messages
from django.http import Http404
from django.shortcuts import redirect, render
from django.urls import reverse

from users.forms import RegisterForm


def login_page(request):
    return render(request, 'users/pages/login.html')


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
