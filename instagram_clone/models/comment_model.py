from django.contrib.auth.models import User
from django.db import models
from .post_model import Post


class Comment(models.Model):
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True
    )
    post = models.ForeignKey(
        Post, on_delete=models.SET_NULL, null=True
    )

    def __str__(self):
        return self.description
