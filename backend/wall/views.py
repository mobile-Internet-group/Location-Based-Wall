from django.shortcuts import render

from rest_framework import viewsets
from wall.models import Walls
from wall.serializer import WallsSerializer
# Create your views here.

class WallsViewSet(viewsets.ModelViewSet):
    queryset = Walls.objects.all()
    serializer_class = WallsSerializer
