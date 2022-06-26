from rest_framework.response import Response
from rest_framework.views import APIView

from core.models import Car
from core.permissions import IsInspector
from inspector.serializers import CarFinishedSerializer


class CarFinished(APIView):

    permission_classes = [IsInspector]

    def post(self, request, id):
        car_obj = Car.objects.get(id=id)
        car_obj.is_finished = True
        car_obj.save()
        serializer = CarFinishedSerializer(car_obj)

        return Response(serializer.data)