from django.urls import path

from inspector.views import CarFinished

urlpatterns = [
    path('car-finished/<int:id>', CarFinished.as_view(), name='car-finished'),
]
