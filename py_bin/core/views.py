from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets, permissions

from .models import Bin
from .serializers import *

class BinViewSet(viewsets.ModelViewSet):
    queryset = Bin.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = BinSerializer
