from django.shortcuts import render
from django.urls import reverse_lazy
from users.models import User, Company
from services.models import Service
from services.models import RequestService
from users.forms import UserLoginForm  
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'users/home.html', {'user': request.user})

@login_required
def customer_profile(request, name):
    user = get_object_or_404(User, username=name)  # Get user by name or show 404
    requested_services = RequestService.objects.filter(customer=user)  # Fetch services

    return render(request, "users/profile.html", {
        "user": user,
        "requested_services": requested_services
    })
#reminder
#update all details to be displayed on both customer and company profiles
    

@login_required
def company_profile(request, name):
    # fetches the company user and all of the services available by it
    user = User.objects.get(username=name)

    services = Service.objects.filter(
        company=Company.objects.get(user=user)).order_by("-date")

    return render(request, 'users/profile.html', {'user': user, 'services': services})

