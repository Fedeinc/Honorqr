from django.test import TestCase
from django.contrib.auth.models import User
from tribute_wall_service.models import Tribute
from profiles.models import Profile
from rest_framework.test import APIClient
from rest_framework import status

class TributeWallManagementTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)
        self.profile = Profile.objects.create(user=self.user, name='John Doe')

    def test_post_tribute(self):
        data = {
            'profile_id': self.profile.id,
            'message': 'This is a tribute message.'
        }
        response = self.client.post('/tributes/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Tribute.objects.filter(profile=self.profile, user=self.user).exists())

    def test_retrieve_tributes(self):
        Tribute.objects.create(profile=self.profile, user=self.user, message='First tribute')
        Tribute.objects.create(profile=self.profile, user=self.user, message='Second tribute')
        response = self.client.get(f'/tributes/{self.profile.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_delete_tribute(self):
        tribute = Tribute.objects.create(profile=self.profile, user=self.user, message='This is a tribute message.')
        response = self.client.delete(f'/tributes/{tribute.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Tribute.objects.filter(id=tribute.id).exists())
