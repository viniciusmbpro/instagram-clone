from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url='users:login_page', redirect_field_name='next')
def home(request):
    return render(request, 'instagram_clone/pages/home.html', {
        'range': range(10),
    })
