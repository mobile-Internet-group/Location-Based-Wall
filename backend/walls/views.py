from django.shortcuts import render

# Create your views here.
# walls/views.py
from rest_framework import viewsets

from walls.models import Walls
from walls.serializer import WallsSerializer


class WallsViewSet(viewsets.ModelViewSet):
    queryset = Walls.objects.all()
    serializer_class = WallsSerializer