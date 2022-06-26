from rest_framework import serializers

from core.models import Car, CarPart


class PartSerializer(serializers.ModelSerializer):

    class Meta:
        model = CarPart
        fields = ['part_name']


class ReceptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car
        fields = '__all__'


class ReceptionDetailSerializer(serializers.ModelSerializer):

    part = PartSerializer(read_only=True, many=True)

    class Meta:
        model = Car
        fields = ['car_name', 'part', 'is_finished', 'is_repair']


class PartListSerializer(serializers.ModelSerializer):

    class Meta:
        model = CarPart
        fields = '__all__'
