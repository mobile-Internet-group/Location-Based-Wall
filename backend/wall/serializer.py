from rest_framework import serializers
from wall.models import Walls

class WallsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Walls
        fields = '__all__'
