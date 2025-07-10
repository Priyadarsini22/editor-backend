# editor/models.py
from django.db import models
from django.contrib.auth.models import User

class Document(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    is_public = models.BooleanField(default=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
