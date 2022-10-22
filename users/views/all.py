from django.shortcuts import render


def login_page(request):
    return render(request, 'users/pages/login.html')


def signup_page(request):
    return render(request, 'users/pages/signup.html')
