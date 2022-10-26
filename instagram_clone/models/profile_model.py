from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(default='', blank=True)
    phone = models.CharField(max_length=100)
    photo = models.ImageField(
        upload_to='instagram_clone/profile_photos/', blank=True, default='')
    gender = models.CharField(max_length=20)
    website = models.CharField(max_length=100)