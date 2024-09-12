from django.contrib import admin
from .models import Profile  # Make sure Profile is correctly defined in models.py

# Register the Profile model if it exists in models.py
try:
    admin.site.register(Profile)
except admin.sites.AlreadyRegistered:
    pass  # Handle the case where the model is already registered
