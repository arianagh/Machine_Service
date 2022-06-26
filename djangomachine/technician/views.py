from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from core.models import Car, CarPart
from core.permissions import IsTechnician
from technician.serializers import CarRepairedSerializer, CarPartSerializer


class CarRepaired(APIView):

    permission_classes = [IsTechnician]

    def post(self, request, id):
        car_obj = Car.objects.get(id=id)
        print(car_obj)
        serializer = CarRepairedSerializer(data=request.data)
        if serializer.is_valid():

            if serializer.validated_data['is_repair'] == True:
                car_obj.is_repair = True
                car_obj.save()
                return Response(status=status.HTTP_201_CREATED)

            elif serializer.validated_data['is_repair'] == False:
                car_obj.is_repair = False
                car_obj.save()
                return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)


class CarPartAdd(APIView):

    permission_classes = [IsTechnician]

    def post(self, request, car_name, part_name):
        car_obj = Car.objects.get(car_name=car_name)
        part_obj = CarPart.objects.get(part_name=part_name)
        serializer = CarPartSerializer(data=request.data)
        if serializer.is_valid():
            car_obj.part.add(part_obj)
            return Response(status=201)
        return Response(serializer.errors)


class CarPartRemove(APIView):

    permission_classes = [IsTechnician]

    def post(self, request, car_name, part_name):
        car_obj = Car.objects.get(car_name=car_name)
        part_obj = CarPart.objects.get(part_name=part_name)
        serializer = CarPartSerializer(data=request.data)
        if serializer.is_valid():
            car_obj.part.remove(part_obj)
            return Response(status=201)
        return Response(serializer.errors)
