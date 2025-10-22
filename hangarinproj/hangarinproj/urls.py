from django.contrib import admin
from django.urls import path, include
from hangarinapp import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Root URL handles authentication check
    path('', views.root_redirect, name='root'),

    # Your app URLs
    path('app/', include('hangarinapp.urls')),

    # Allauth URLs for login, logout, signup, social auth
    path('accounts/', include('allauth.urls')),

    # PWA URLs for offline and installable features
    path('', include('pwa.urls')),  # This should be at the bottom
]
