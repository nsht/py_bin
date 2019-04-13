import string
import random
import time

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets, permissions

from .models import Bin
from .serializers import *
from .utils import generate_slug
import pdb


class BinViewSet(viewsets.ModelViewSet):
    queryset = Bin.objects.all().filter(protected=False, is_public=True)
    permission_classes = [permissions.AllowAny]
    serializer_class = BinSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

    def perform_create(self, serializer):
        serializer.save()


# TODO
# Add login
# Add JWT authentication
# Add Views
