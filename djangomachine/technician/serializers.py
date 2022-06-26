from rest_framework import serializers

from core.models import Car


class CarRepairedSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car
        fields = ['is_repair']


class CarPartSerializer(serializers.ModelSerializer):

    part = serializers.CharField(source='part.part_name')

    class Meta:
        model = Car
        fields = ['part', 'car_name']






