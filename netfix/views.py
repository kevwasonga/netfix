from django.shortcuts import render
from django.urls import reverse_lazy
from users.models import User, Company
from services.models import Service
from users.views import User
from users.forms import UserLoginForm  
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login


def home(request):
    return render(request, 'users/home.html', {'user': request.user})


def customer_profile(request, name):
    return render(request, "users/profile.html", {"username": name})
#reminder
#update all details to be displayed on both customer and company profiles
    


def company_profile(request, name):
    # fetches the company user and all of the services available by it
    user = User.objects.get(username=name)

    services = Service.objects.filter(
        company=Company.objects.get(user=user)).order_by("-date")

    return render(request, 'users/profile.html', {'user': user, 'services': services})

