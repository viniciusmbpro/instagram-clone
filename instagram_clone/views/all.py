from django.shortcuts import render


def home(request):
    return render(request, 'instagram_clone/pages/home.html', {
        'range': range(10),
    })
