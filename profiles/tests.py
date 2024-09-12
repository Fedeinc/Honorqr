# profiles/tests.py
from django.test import TestCase
from .models import Profile

class ProfileModelTest(TestCase):
    def test_profile_creation(self):
        profile = Profile.objects.create(name="Test Profile")
        self.assertEqual(profile.name, "Test Profile")
