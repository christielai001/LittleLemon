from django.test import TestCase
from restaurant.models import Menu

class MenuTest(TestCase):
    def test_get_item(self):
        # Create a menu item
        item = Menu.objects.create(Title="Pasta", Price=12.99, Inventory=100)
        
        # Check if the serialized data matches the expected output
        self.assertEqual(str(item), "Pasta : 12.99")

