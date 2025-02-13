"""
URL configuration for netfix project.

Routes URLs to views:
- Django Admin Panel
- Main app (homepage)
- Services app
- Users app (authentication & profiles)
- Customer & Company profile views
"""

from django.contrib import admin
from django.urls import include, path
from users import views as v  # Import views from users app

urlpatterns = [
    path('admin/', admin.site.urls),  # ✅ Django Admin Panel
    path('', include('main.urls')),  # ✅ Homepage & main app
    path('services/', include('services.urls')),  # ✅ Service-related routes
    path('users/', include('users.urls')),  # ✅ Handles registration & profiles
    
    # ✅ Profile pages (Updated Naming)
    path('customer/<str:username>/', v.CustomerProfileView, name='customer_profile'),
    path('company/<str:username>/', v.CompanyProfileView, name='company_profile'),
]
