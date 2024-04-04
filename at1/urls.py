from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('flashcards.urls')),  # Include flashcards app URLs
    path('users/', include('users.urls')),  # Include users app URLs
    path('eduprod/', include('eduprod.urls')),  # Include eduprod app URLs
    path('', include('splash.urls')),  # Include splash app URLs
    # Add other URL patterns as needed
    path('accounts/', include('django.contrib.auth.urls')),  # Include built-in authentication URLs
    
]