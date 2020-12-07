from django.db import models
# We want to get notified when a new user gets created, so we can automate the token creation for new users
from django.db.models.signals import post_save
# a decorator we will use to know when a new user is created
from django.dispatch import receiver
# Token we want to create in DB for new users
from rest_framework.authtoken.models import Token
from django.conf import settings

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

    # blank property does not need migrations (since server sends empty string, but null will require migrations!
    middleName=models.CharField(max_length=20,blank=True,null=True)
    lastName=models.CharField(max_length=20)
    email=models.CharField(max_length=30)
    phoneNumber=models.CharField(max_length=10)

class Reservation(models.Model):
    # Between Flights and Reservation we have OneToMany relationship, which can be specified by declaring Flight
    # as ForeignKey in this class!
    # If flight itself gets deleted, we want reservation to be deleted as well
    flight = models.ForeignKey(Flight,on_delete=models.CASCADE)
    passenger = models.OneToOneField(Passenger,on_delete=models.CASCADE)

# Our handler method to create and save token when a new user is created
# AUTH_USER_MODEL is managed by DRF, serves to store users for our app
# method name is not important here but the annotation (decorator) and method arguments need to be coded as it is!
@receiver(post_save,sender=settings.AUTH_USER_MODEL)
def createAuthToken(sender,instance,created,**kwargs):
    if created:
        # Create and save a token in DB, associate it with user as instance
        Token.objects.create(user=instance)
