from django.urls import path
from django.contrib.auth import views

from .forms import UserLoginForm
from . import views as v
urlpatterns = [
    path('register_company/', v.CompanySignUpView.as_view(), name='register_company'),
    path('register_customer/', v.CustomerSignUpView.as_view(), name='register_customer'),
    path("profile/<int:pk>/", v.UserProfileView.as_view(), name="user_profile"),
    path('', v.register, name='register'),

]
