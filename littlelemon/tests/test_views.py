from django.test import TestCase
from rest_framework.test import APIClient
from restaurant.models import Menu # Use MenuItem consistently
from restaurant.serializers import MenuItemSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        # Create sample data in the test database
        Menu.objects.create(title="Burger", price=10.99, inventory=50)
        Menu.objects.create(title="Pizza", price=12.99, inventory=40)

    def test_getall(self):
        # Use the exact URL from your urls.py
        response = self.client.get('/restaurant/menu/') 
        
        # Get data from database and serialize it
        menu_items = Menu.objects.all()
        serializer = MenuItemSerializer(menu_items, many=True)
        
        # Compare
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer.data)