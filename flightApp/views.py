from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Flight, Passenger, Reservation
from .serializers import FlightSerializer, PassengerSerializer, ReservationSerializer

# Create your views here.

# Function based view for findFlight endpoint
@api_view(["POST"])
def findFlights(request: Request):
    flights = Flight.objects.filter(
        departureCity=request.data["departureCity"],
        arrivalCity=request.data["arrivalCity"],
        dateOfDeparture=request.data["dateOfDeparture"],
    )
    serializer = FlightSerializer(flights, many=True)

    return Response(serializer.data)


# ViewSet based views
class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer


class PassengerViewSet(viewsets.ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
