from django.urls import path
from . import views  # This imports your views file
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),  # Basic URL pattern for your app's index view
    path('login/', auth_views.LoginView.as_view(), name='login'),  # Login URL pattern
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Logout URL pattern
]
