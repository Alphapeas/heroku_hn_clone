from django.db import models

from user.models import User


class Post(models.Model):
    """News post"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=300)
    link = models.URLField(blank=True)
    content = models.CharField(max_length=1000, blank=True)
    votes = models.ManyToManyField(User, related_name='vote', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
