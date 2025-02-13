from django.urls import path
from .views import field_services_view, services_list_view, request_service_view, single_service_view

urlpatterns = [
    path('', services_list_view, name='services_list'),
    path('<str:field>/', field_services_view, name='field_services'),
    path('<int:id>/', single_service_view, name='single_service'),
    path('<int:id>/request/', request_service_view, name='request_service'),
]
