import json

from django.test import TestCase
from flightApp.models import Flight, Passenger, Reservation


class flightServicesViewTest(TestCase):
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

    def test_flight_get_view(self):

        response = self.client.get("/flightServices/flights/")
        self.assertEqual(response.status_code, 200)
        result = json.loads(response.content)

        assert len(result) == 1
        assert result[0]["airline"] == "Lufthansa"

    def test_passenger_get_view(self):

        response = self.client.get("/flightServices/passengers/")
        self.assertEqual(response.status_code, 200)
        result = json.loads(response.content)

        assert len(result) == 1
        assert result[0]["firstName"] == "Jane"

    def test_flight_post_view(self):
        post_data = {
            "flightNumber": "A123",
            "airline": "Lufthansa",
            "departureCity": "New York",
            "arrivalCity": "Munich",
            "dateOfDeparture": "2020-11-28",
            "timeOfDeparture": "12:00:00",
        }
        response = self.client.post("/flightServices/flights/", post_data)
        self.assertEqual(response.status_code, 201)
        result = json.loads(response.content)

        assert result["flightNumber"] == post_data["flightNumber"]

    def test_passenger_post_view(self):
        post_data = {
            "firstName": "James",
            "lastName": "Bond",
            "middleName": "",
            "email": "bond@mi.com",
            "phone": "1213",
        }
        response = self.client.post("/flightServices/passengers/", post_data)
        self.assertEqual(response.status_code, 201)
        result = json.loads(response.content)

        assert result["firstName"] == post_data["firstName"]
        assert result["lastName"] == post_data["lastName"]

    def test_get_flight_detail_unknown_id(self):
        response = self.client.get("/flightServices/flights/100/")
        self.assertEqual(response.status_code, 404)

    def test_get_passenger_detail_unknown_id(self):
        response = self.client.get("/flightServices/passengers/100/")
        self.assertEqual(response.status_code, 404)

    def test_get_flight_detail_by_id(self):

        response = self.client.get("/flightServices/flights/")
        self.assertEqual(response.status_code, 200)
        result = json.loads(response.content)

        response = self.client.get(f"/flightServices/flights/{result[0]['id']}/")
        self.assertEqual(response.status_code, 200)

    def test_get_passenger_detail_by_id(self):

        response = self.client.get("/flightServices/passengers/")
        self.assertEqual(response.status_code, 200)
        result = json.loads(response.content)

        response = self.client.get(f"/flightServices/passengers/{result[0]['id']}/")
        self.assertEqual(response.status_code, 200)

    def test_delete_flight_detail(self):

        response = self.client.get("/flightServices/flights/")
        self.assertEqual(response.status_code, 200)
        result = json.loads(response.content)

        response = self.client.delete(f"/flightServices/flights/{result[0]['id']}/")
        self.assertEqual(response.status_code, 204)

        # Confirm that the deleted entry doesn't exist anymore
        response = self.client.get(f"/flightServices/flights/{result[0]['id']}/")
        self.assertEqual(response.status_code, 404)

    def test_delete_passenger_detail(self):

        response = self.client.get("/flightServices/passengers/")
        self.assertEqual(response.status_code, 200)
        result = json.loads(response.content)

        response = self.client.delete(f"/flightServices/passengers/{result[0]['id']}/")
        self.assertEqual(response.status_code, 204)

        # Confirm that the deleted entry doesn't exist anymore
        response = self.client.get(f"/flightServices/passengers/{result[0]['id']}/")
        self.assertEqual(response.status_code, 404)
