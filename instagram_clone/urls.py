from django.urls import path

from instagram_clone import views

app_name = "insta"

urlpatterns = [
    path('', views.home, name='home'),
]
