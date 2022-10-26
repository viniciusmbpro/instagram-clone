from django.urls import path

from instagram_clone import views

app_name = "insta"

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('profile/<int:id>/edit/', views.profile_edit, name='profile_edit'),
    path('post/like/', views.post_like, name='post_like'),
    path('post/<int:id>/edit', views.post_edit, name='post_edit'),
    path('post/new/', views.post_new, name='post_new'),
]
