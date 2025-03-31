from django.test import TestCase
from rest_framework.test import APIClient
from restaurant.models import Menu

class MenuItemViewTest(TestCase):
    def setUp(self):
        # Create an instance of APIClient for DRF testing
        self.client = APIClient()
        
        # Create test data
        self.item1 = Menu.objects.create(Title="Pasta", Price=12.99, Inventory=100)
        self.item2 = Menu.objects.create(Title="Pizza", Price=8.99, Inventory=50)
        self.item3 = Menu.objects.create(Title="Salad", Price=5.99, Inventory=20)
    
    def test_getall(self): 
        # The URL where Menu API is retrieved
        response = self.client.get('/restaurant/menu/')
        
        # Check if the response status code is 200 OK
        self.assertEqual(response.status_code, 200)
        
        # verify the response data using serialized data to match the Menu items
        self.assertEqual(len(response.data), 3)
        self.assertEqual(response.data[0]['Title'], self.item1.Title)
        self.assertEqual(response.data[1]['Title'], self.item2.Title)
        self.assertEqual(response.data[2]['Title'], self.item3.Title)
