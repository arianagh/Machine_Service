from rest_framework import permissions
from rest_framework.generics import RetrieveAPIView

from core.permissions import IsInspector, IsReception, IsTechnician, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from car.serializers import ReceptionSerializer, ReceptionDetailSerializer, PartListSerializer
from core.models import Car, CarPart


class CarListView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        qs = Car.objects.all()
        print(qs)
        serializer = ReceptionSerializer(qs, many=True)
        return Response(serializer.data)


class CarDetailView(RetrieveAPIView):

    permission_classes = [IsAuthenticated]
    queryset = Car.objects.all()
    serializer_class = ReceptionDetailSerializer


class PartListView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        qs = CarPart.objects.all()
        serializer = PartListSerializer(qs, many=True)
        return Response(serializer.data)
