from rest_framework import serializers
from flightApp.models import Flight,Passenger,Reservation
import re

'''
Note: You can use built-in validations from Django in model class itself like max_length, null=True, etc.
If you want to use your own validators, there are 3 ways of doing it in serializers.py:
1) Add methods like validate_XXX inside a specific serializer class, like validate_flightNumber method in this file.
   This method is called first when serializer.isValid() is checked by the server.
   In this method, you get specific field data passed with request since method is coded for a specific field as it is
   obvious from method names themselfves, like validate_departureCity(self, request)!
2) Next, you can add your own method outside of serializer class, which take data as dictionary of entire data that comes
   with request object. No specific naming scheme is required here.
   How does Django knows about these methods?
   By us speficying this method in spefic serializer class with attribute: validators=['method_name1', 'etc']
   This method is called next.
3) Finally, there is "catch all" validator that you can add in the serializer class itself with a defined name, i.e.,
   validate. This takes self (since itside the class) and data dictionary, that comes with request.
   Note: from data dictionary, you can retrieve specific field and do your own validations, return ValidationError, etc.
   This method is called as last one.

If you run this app and create a flight, you'll see following in the output that are coming from 3 ways of adding
validations in this file itself!
Output sample:
1. validate_XXX methods called first.
2. isFlightNumberValid like methods declared with validators= in Serializer class get called next.
2. Entire request data is passed to validators methods as well:
OrderedDict([('flightNumber', 'U4T35'), ('operatingAirlines', 'Delta'), ('departureCity', 'Amsterdam'),
('arrivalCity', 'LAX'), ('dateOfDeparture', datetime.date(2021, 3, 22)), ('estimatedTimeOfDeparture', datetime.time(5, 55))])
3. validate method called as last one.
3. validate method get entire request data: OrderedDict([('flightNumber', 'U4T35'),
('operatingAirlines', 'Delta'), ('departureCity', 'Amsterdam'), ('arrivalCity', 'LAX'),
('dateOfDeparture', datetime.date(2021, 3, 22)), ('estimatedTimeOfDeparture', datetime.time(5, 55))])
3. got flightNumber from data dictionary at validate method:U4T35
'''
def isFlightNumberValid(data):
    print('2. isFlightNumberValid like methods declared with validators= in Serializer class get called next.')
    print(f'2. Entire request data is passed to validators methods as well: {data}')
    return data

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'
        validators=[isFlightNumberValid]

    # We use DRF built-in validations in Model class but this is how we can add our own custom validations!
    # Note: method name must follow this scheme: <validate_><exact_field_name_from_model>
    # DRF calls these functions at runtime
    def validate_flightNumber(self,flightNumber):
        print('1. validate_XXX methods called first.')

        if re.match("^[a-zA-Z0-9]*$", flightNumber) == None:
            raise serializers.ValidationError("Invalid flightNumber! It must be alpha numeric.")

        return flightNumber

    def validate(self, data):
        print('3. validate method called as last one.')
        print(f'3. validate method get entire request data: {data}')
        print('3. got flightNumber from data dictionary at validate method:' + data['flightNumber'])

        return data

class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = '__all__'

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'
