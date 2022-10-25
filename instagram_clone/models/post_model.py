from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    caption = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(
        upload_to='instagram_clone/post_photos/', blank=True, default='')
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True
    )

    def __str__(self):
        return self.caption
