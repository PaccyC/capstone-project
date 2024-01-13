from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Booking, Menu
from .serializers import BookingSerializer, MenuSerializer

class MenuViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.menu_data = {"name": "Sample Item", "price": 10.99}
        self.menu = Menu.objects.create(**self.menu_data)
        self.menu_url = '/menu/'  # Update with your actual URL

    def test_get_menu_items(self):
        response = self.client.get(self.menu_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_menu_item(self):
        response = self.client.post(self.menu_url, data=self.menu_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class BookingViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.booking_data = {"customer_name": "John Doe", "total_amount": 50.0}
        self.booking = Booking.objects.create(**self.booking_data)
        self.booking_url = '/bookings/'  # Update with your actual URL

    def test_get_bookings(self):
        response = self.client.get(self.booking_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_booking(self):
        response = self.client.post(self.booking_url, data=self.booking_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class BookingViewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.booking_url = '/bookings/'  # Update with your actual URL

    def test_get_bookings(self):
        response = self.client.get(self.booking_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Add more test cases as needed
