import string
import random
import time

from django.contrib.auth.hashers import make_password
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets, permissions

from .models import Bin
from .serializers import *

import pdb


class BinViewSet(viewsets.ModelViewSet):
    queryset = Bin.objects.all().filter(protected=False,private=False)
    permission_classes = [permissions.AllowAny]
    serializer_class = BinSerializer

    def create(self, request):
        slug = self.generate_slug()
        chk_slug = Bin.objects.filter(slug=slug).first()
        # keep generating new slugs until no collitions are detected
        # very low probability of happening twice.
        while chk_slug is not None:
            slug = self.generate_slug()
            chk_slug = Bin.objects.filter(slug=slug).first()
        bin = Bin(
            slug=slug,
            content=request.data.get("content"),
            content_format=request.data.get("content_format"),
        )
        if request.data.get("password") != "":
            bin.protected = True
            bin.is_public = False
            # uses PBKDF2 by default, use check_password to verify passwords
            bin.password = make_password(request.data.get("password"))
        bin.save()
        return Response(status=status.HTTP_200_OK)

    # TODO Move function to helper file
    def generate_slug(self):
        random.seed(time.time())
        chars = string.ascii_letters + string.digits
        return "".join(random.choice(chars) for _ in range(7))
