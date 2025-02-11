from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),  # Home page
    path('logout/', views.logout_view, name='logout'),  # Logout page
]
