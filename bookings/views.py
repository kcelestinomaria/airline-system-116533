from django.shortcuts import render
from rest_framework import viewsets, filters
from .models import Flight, Passenger
from .serializers import FlightSerializer, PassengerSerializer

# Create your views here.

class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    filter_backends = [filters.SearchFilter] # implements filters
    search_fields = ['origin', 'destination']

class PassengerViewSet(viewsets.ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['flight__flight_number']


