from rest_framework import serializers

from core.models import Car


class CarFinishedSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car
        fields = ['car_name', 'is_finished']
        extra_kwargs = {
            "car_name": {"read_only": True}
        }

