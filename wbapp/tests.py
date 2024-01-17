from django.test import TestCase
from django.urls import reverse
from .models import UserProfile
from datetime import datetime

class UserProfileTests(TestCase):
    def setUp(self):
        self.user = UserProfile.objects.create(
            username='testuser',
            address='123 Main St',
            phone='555-1234',
            email='test@example.com',
            created=datetime.now().date(),
        )

    def test_user_profile_creation(self):
        self.assertIsInstance(self.user, UserProfile)
        self.assertEqual(self.user.username, 'testuser')
        self.assertEqual(self.user.address, '123 Main St')
        self.assertEqual(self.user.phone, '555-1234')
        self.assertEqual(self.user.email, 'test@example.com')
        self.assertIsNotNone(self.user.created)
        self.assertIsNotNone(self.user.updated)
    
    def test_user_profile_view(self):
        response = self.client.get(reverse('user_profile', args=[self.user.id]))
        # Check that the response status is 200 (OK)
        self.assertEqual(response.status_code, 200)
        # Check that the context contains the user profile data
        self.assertEqual(response.context['user'].username, 'testuser')
        self.assertEqual(response.context['user'].address, '123 Main St')
        self.assertEqual(response.context['user'].phone, '555-1234')
        self.assertEqual(response.context['user'].email, 'test@example.com')
        # Check that the rendered content contains the user's username
        self.assertContains(response, 'testuser')

    def test_user_profile_view_not_found(self):
        # Try to access a non-existent user profile
        response = self.client.get(reverse('user_profile', args=[999]))
        # Check that the response status is 404 (Not Found)
        self.assertEqual(response.status_code, 404)
