from django.contrib.auth.models import User
from django.db import models

from .post_model import Post


class Like(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True
    )
    post = models.ForeignKey(
        Post, on_delete=models.SET_NULL, null=True
    )
