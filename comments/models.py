from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Comment by {self.user.username} on {self.created_at}'