from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from .models import Menu

class TestMenuViews(TestCase):
    """
    Test to check menu can be viewed
    Tests are derived from The code institute 'I think therefore I blog' module.
    https://learn.codeinstitute.net/
    """
    def setUp(self):
        """Create instance of superuser"""
        self.user = User.objects.create_superuser(
            username="Superuser",
            password="password",
            email="test@test.com"
        )
        
        """Create instance of user"""       
        self.user = User.objects.create_user(
            username="username",
            password="password123!",
            email="test@test.com"
        )
        self.user.save()

        """Add menu item"""
        self.post = Menu(menu_entry_type="Main", menu_entry_by=self.user,
                         menu_entry_name="test name", menu_entry_description="test description",
                         menu_entry_price="9.99")
        self.post.save()


    def test_render_menu_view(self):
        """Confirm menu item can be seen without logging in."""
        response = self.client.get(reverse('menu'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"main", response.content)
        self.assertIn(b"test name", response.content)
        self.assertIn(b"test description", response.content)
        self.assertIn(b"9.99", response.content)


    def test_render_menu_view_login(self):
        """Confirm menu item can be seen after logging in."""
        self.client.login(username='username', password='password123!')
        response = self.client.get(reverse('menu'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"main", response.content)
        self.assertIn(b"test name", response.content)
        self.assertIn(b"test description", response.content)
        self.assertIn(b"9.99", response.content)
