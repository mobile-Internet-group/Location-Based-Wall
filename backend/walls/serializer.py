# walls/serializer.py
from rest_framework import serializers

from walls.models import Walls

class WallsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Walls
        fields = '__all__'