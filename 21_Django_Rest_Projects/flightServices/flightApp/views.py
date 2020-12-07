from django.shortcuts import render
from flightApp.models import Flight,Passenger,Reservation
from flightApp.serializers import FlightSerializer,PassengerSerializer,ReservationSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

# Custom views using Function Based Views
@api_view(['POST'])
def find_flights(request):
    flights = Flight.objects.filter(departureCity=request.data['departureCity'],
              arrivalCity=request.data['arrivalCity'],dateOfDeparture=request.data['dateOfDeparture'])
    serializer=FlightSerializer(flights,many=True)
    return Response(serializer.data)

# Below method allow us to create a reservation and create new passenger on the fly
# Params need to be passed:
# A (valid) flightId with new passenger data(firstName, middleName, lastName, email and phoneNumber)
@api_view(['POST'])
def save_reservation(request):

    # Retrieve flight object
    flight = Flight.objects.get(id=request.data['flightId'])

    # Let's create a passenger object based on request.data
    passenger = Passenger()
    passenger.firstName = request.data['firstName']
    passenger.middleName = request.data['middleName']
    passenger.lastName = request.data['lastName']
    passenger.email = request.data['email']
    passenger.phoneNumber = request.data['phoneNumber']
    # Let's save the passenger first before saving it with reservation
    passenger.save()

    # Create a new reservation and save it to DB
    reservation = Reservation()
    reservation.flight = flight
    reservation.passenger = passenger
    reservation.save()

    # Return status code HTTP_201_CREATED
    return Response(status=status.HTTP_201_CREATED)

# Class based views for regular CRUD functionality
class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    permission_classes = (IsAuthenticated,)  # Note: a comma is needed at the end!

class PassengerViewSet(viewsets.ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
