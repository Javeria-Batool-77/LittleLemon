from django.test import TestCase
from restaurant.models import Menu

class MenuItemTest(TestCase):
    def test_get_item(self):
        # Create the object
        item = Menu.objects.create(title="Bakhlava", price=10.00, inventory=100)
        # Convert to string and compare
        self.assertEqual(str(item), "Bakhlava : 10.0")