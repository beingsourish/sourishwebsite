from rest_framework import serializers
from .models import PlacesVisited

class PlacesVisitedSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlacesVisited
        fields = '__all__'
