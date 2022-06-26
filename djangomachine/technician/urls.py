from django.urls import path

from technician.views import CarRepaired, CarPartAdd, CarPartRemove

urlpatterns = [
    path('car-repaired/<int:id>', CarRepaired.as_view(), name='car-repaired'),
    path('add-car-part/<slug:car_name>/<slug:part_name>/', CarPartAdd.as_view(), name='add-car-part'),
    path('remove-car-part/<slug:car_name>/<slug:part_name>/', CarPartRemove.as_view(), name='remove-car-part'),
]
