from rest_framework import serializers

from core.models import Car


class CarCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car
        fields = ['car_name']

