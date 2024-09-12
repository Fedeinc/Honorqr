from django.test import TestCase
from django.contrib.auth.models import User
from qr_code_service.models import QRCode
from profiles.models import Profile
from rest_framework.test import APIClient
from rest_framework import status

class QRCodeManagementTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)
        self.profile = Profile.objects.create(user=self.user, name='John Doe')

    def test_generate_qr_code(self):
        data = {
            'profile_id': self.profile.id
        }
        response = self.client.post('/qrcodes/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(QRCode.objects.filter(profile=self.profile).exists())

    def test_retrieve_qr_code(self):
        qr_code = QRCode.objects.create(profile=self.profile, qr_code_data='sample_data')
        response = self.client.get(f'/qrcodes/{qr_code.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['qr_code_data'], 'sample_data')

    def test_delete_qr_code(self):
        qr_code = QRCode.objects.create(profile=self.profile, qr_code_data='sample_data')
        response = self.client.delete(f'/qrcodes/{qr_code.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(QRCode.objects.filter(id=qr_code.id).exists())
