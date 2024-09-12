from django.test import TestCase
from django.contrib.auth.models import User
from profiles.models import Profile
from rest_framework.test import APIClient
from rest_framework import status

class ProfileManagementTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)

    def test_create_profile(self):
        data = {
            'name': 'John Doe',
            'date_of_birth': '1990-01-01',
            'biography': 'A short bio.'
        }
        response = self.client.post('/profiles/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Profile.objects.filter(user=self.user).exists())

    def test_update_profile(self):
        profile = Profile.objects.create(user=self.user, name='John Doe')
        data = {
            'name': 'John Updated',
            'biography': 'Updated bio.'
        }
        response = self.client.put(f'/profiles/{profile.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        profile.refresh_from_db()
        self.assertEqual(profile.name, 'John Updated')

    def test_delete_profile(self):
        profile = Profile.objects.create(user=self.user, name='John Doe')
        response = self.client.delete(f'/profiles/{profile.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Profile.objects.filter(id=profile.id).exists())
