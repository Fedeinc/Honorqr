from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('auth_service.urls')),
    path('notifications/', include('notification_service.urls')),
    path('profiles/', include('profiles.urls')),
    path('qr/', include('qr_code_service.urls')),
    path('tribute/', include('tribute_wall_service.urls')),
    path('user/', include('user_profile_service.urls')),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    # Add more URL patterns as needed
]

# This adds static file handling in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)