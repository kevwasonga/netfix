from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .models import CustomerProfile, CompanyProfile, CustomUser
from services.models import Service, ServiceRequest
from .forms import CustomerRegistrationForm, CompanyRegistrationForm

# ✅ Register Selection Page
def register(request):
    return render(request, "users/register.html")

# ✅ Register a Customer
def register_customer(request):
    if request.method == "POST":
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("user_profile")
    else:
        form = CustomerRegistrationForm()
    return render(request, "users/register_customer.html", {"form": form})

# ✅ Register a Company
def register_company(request):
    if request.method == "POST":
        form = CompanyRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("user_profile")
    else:
        form = CompanyRegistrationForm()
    return render(request, "users/register_company.html", {"form": form})

# ✅ User Profile Page
@login_required
def user_profile(request):
    user = request.user
    context = {"user": user}

    if user.is_customer:
        profile = get_object_or_404(CustomerProfile, user=user)  
        requested_services = ServiceRequest.objects.filter(customer=profile)  # 🔥 FIX APPLIED (Used `profile` instead of `user`)
        context.update({"profile": profile, "requested_services": requested_services})

    elif user.is_company:
        profile = get_object_or_404(CompanyProfile, user=user)
        company_services = Service.objects.filter(company=profile)  # 🔥 FIX APPLIED (Used `profile` instead of `user`)
        context.update({"profile": profile, "company_services": company_services})

    return render(request, "users/profile.html", context)

# ✅ Customer Profile View
@login_required
def CustomerProfileView(request, username):
    """ Display a customer's profile and their requested services """
    user = get_object_or_404(CustomUser, username=username)
    profile = get_object_or_404(CustomerProfile, user=user)
    requested_services = ServiceRequest.objects.filter(customer=profile)  # 🔥 FIX APPLIED (Used `profile` instead of `user`)

    return render(request, "users/profile.html", {
        "profile": profile,
        "requested_services": requested_services,
        "is_customer": True
    })

# ✅ Company Profile View
def CompanyProfileView(request, username):
    """ Displays a company's profile and its offered services """
    user = get_object_or_404(CustomUser, username=username)
    
    # Ensure user has a company profile
    if not hasattr(user, "company_profile"):
        return render(request, "users/company_not_found.html")  # Error page if no company profile exists

    profile = user.company_profile
    company_services = Service.objects.filter(company=profile)  # 🔥 FIX APPLIED (Used `profile` instead of `user`)

    return render(request, "users/company_profile.html", {
        "profile": profile,
        "company_services": company_services,
        "is_company": True
    })

# ✅ Debugging CSRF Issues
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt  # ❌ Not recommended for production
def my_view(request):
    return render(request, "users/login.html")
