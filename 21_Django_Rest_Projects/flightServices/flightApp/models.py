from django.db import models

# Create your models here.
class Flight(models.Model):
    flightNumber=models.CharField(max_length=10)
    operatingAirlines=models.CharField(max_length=20)
    departureCity=models.CharField(max_length=20)
    arrivalCity=models.CharField(max_length=20)
    dateOfDeparture=models.DateField()
    estimatedTimeOfDeparture=models.TimeField()

class Passenger(models.Model):
    firstName=models.CharField(max_length=20)
    middleName=models.CharField(max_length=20)
    lastName=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    phoneNumber=models.CharField(max_length=10)

class Reservation(models.Model):
    # If flight itself gets deleted, we want reservation to be deleted as well
    flight = models.OneToOneField(Flight,on_delete=models.CASCADE)
    passenger = models.OneToOneField(Passenger,on_delete=models.CASCADE)
