from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Bin(models.Model):
    slug = models.CharField(max_length=10, unique=True)
    content = models.TextField()
    content_format = models.CharField(max_length=10)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    view_count = models.IntegerField(max_length=300, null=True, blank=True)
    status = models.IntegerField(max_length=5)
    protected = models.BooleanField()
    password = models.CharField(max_length=50)
    expiry = models.DateTimeField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.slug
