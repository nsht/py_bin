from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator

# Create your models here.


class Bin(models.Model):
    slug = models.CharField(max_length=10, unique=True,blank=True)
    content = models.TextField()
    content_format = models.CharField(max_length=10)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(null=True, blank=True)
    view_count = models.IntegerField(default=0)
    status = models.IntegerField(validators=[MaxValueValidator(5)],default=1)
    protected = models.BooleanField(default=False)
    is_public = models.BooleanField(default=True)
    password = models.CharField(max_length=50,null=True, blank=True)
    expiry = models.DateTimeField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.slug
