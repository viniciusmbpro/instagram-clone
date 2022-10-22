from django.urls import path

from users import views

app_name = "users"

urlpatterns = [
    path('login/', views.login_page, name='login'),
    path('login/create/', views.login_create, name='login_create'),
    path('signup/', views.signup_page, name='signup'),
    path('signup/create/', views.signup_create, name='signup_create'),
]
