import string
import random
import time

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets, permissions

from .models import Bin
from .serializers import *


class BinViewSet(viewsets.ModelViewSet):
    # TODO only show public objects
    queryset = Bin.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = BinSerializer

    def create(self, request):
        # TODO check for slug collisions
        slug = self.generate_slug()
        bin = Bin(
            slug=slug,
            content=request.data.get("content"),
            content_format=request.data.get("content_format"),
        )
        bin.save()
        import pdb
        pdb.set_trace()
        return Response(status=status.HTTP_200_OK)

# TODO Move function to helper file
    def generate_slug(self):
        random.seed(time.time())
        chars = string.ascii_letters + string.digits
        return "".join(random.choice(chars) for _ in range(7))
