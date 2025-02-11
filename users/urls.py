from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile_view, name='profile'),
    path('register/', views.register_view, name='register'),
    path('register/customer/', views.register_customer, name='register_customer'),
    path('register/company/', views.register_company, name='register_company'),
]
