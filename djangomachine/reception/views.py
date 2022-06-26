from rest_framework import status
from rest_framework.generics import UpdateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from core.models import Car
from core.permissions import IsReception

from reception.serializers import CarCreateSerializer


class CarCreateView(APIView):

    permission_classes = [IsReception]

    def post(self, request):
        serializer = CarCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)


class CarUpdateView(UpdateAPIView):

    permission_classes = [IsReception]
    queryset = Car.objects.all()
    serializer_class = CarCreateSerializer
