# Example for other services, e.g., `auth_service/views.py`

from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome to the Auth Service!")
