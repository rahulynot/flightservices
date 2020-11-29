from django.test import TestCase
from flightApp.models import Flight, Passenger, Reservation

# Create your tests here.


class flightServicesModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Flight.objects.create(
            flightNumber="1",
            airline="Lufthansa",
            departureCity="Essen",
            arrivalCity="Paris",
            dateOfDeparture="2020-10-25",
            timeOfDeparture="12:00",
        )

        Passenger.objects.create(
            firstName="Jane", lastName="Doe", email="jane@email.com", phone="1234567890"
        )

    def test_flight_model(self):
        flight = Flight.objects.get(flightNumber="1")
        flightNumber = flight._meta.get_field("flightNumber").verbose_name
        airline = flight._meta.get_field("airline").verbose_name
        departureCity = flight._meta.get_field("departureCity").verbose_name
        arrivalCity = flight._meta.get_field("arrivalCity").verbose_name
        dateOfDeparture = flight._meta.get_field("dateOfDeparture").verbose_name
        timeOfDeparture = flight._meta.get_field("timeOfDeparture").verbose_name

        self.assertEqual(flightNumber, "flightNumber")
        self.assertEqual(airline, "airline")
        self.assertEqual(departureCity, "departureCity")
        self.assertEqual(arrivalCity, "arrivalCity")
        self.assertEqual(dateOfDeparture, "dateOfDeparture")
        self.assertEqual(timeOfDeparture, "timeOfDeparture")

    def test_passenger_model(self):
        passenger = Passenger.objects.get(firstName="Jane")
        firstName = passenger._meta.get_field("firstName").verbose_name
        middleName = passenger._meta.get_field("middleName").verbose_name
        lastName = passenger._meta.get_field("lastName").verbose_name
        email = passenger._meta.get_field("email").verbose_name
        phone = passenger._meta.get_field("phone").verbose_name

        self.assertEqual(firstName, "firstName")
        self.assertEqual(middleName, "middleName")
        self.assertEqual(lastName, "lastName")
        self.assertEqual(email, "email")
        self.assertEqual(phone, "phone")
