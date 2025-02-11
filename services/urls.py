from django.urls import path
from . import views

urlpatterns = [
    path('', views.services_list_view, name='services_list'),  # List all services
    path('field/<str:field>/', views.field_services_view, name='field_services'),  # Filter by field
    path('<int:id>/', views.single_service_view, name='single_service'),  # Single service details
    path('<int:id>/request/', views.request_service_view, name='request_service'),  # Request service
]
