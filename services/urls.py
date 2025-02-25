from django.urls import path
from . import views as v

urlpatterns = [
    path('', v.service_list, name='service_list'),
    path('create/', v.create, name='create'),
    path('<int:id>', v.index, name='index'),
    path('<int:service_id>/request_service/', v.request_service, name='request_service'),
    path('<slug:field>/', v.service_field, name='services_field'),
]
