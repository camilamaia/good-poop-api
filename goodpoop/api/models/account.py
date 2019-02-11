from django.db import models


class Account(models.Model):
    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
