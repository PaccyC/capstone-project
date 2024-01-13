from django.test import TestCase
from .models import Menu, Booking

class MenuModelTest(TestCase):
    def setUp(self):
        Menu.objects.create(item='Sample Item', price=10)

    def test_menu_item(self):
        menu_item = Menu.objects.get(item='Sample Item')
        self.assertEqual(menu_item.item, 'Sample Item')
        self.assertEqual(menu_item.price, 10)

    def test_menu_item_str_representation(self):
        menu_item = Menu.objects.get(item='Sample Item')
        self.assertEqual(str(menu_item), 'Sample Item')

class BookingModelTest(TestCase):
    def setUp(self):
        Booking.objects.create(tableno=1, people=4)

    def test_booking_details(self):
        booking_details = Booking.objects.get(tableno=1)
        self.assertEqual(booking_details.tableno, 1)
        self.assertEqual(booking_details.people, 4)
