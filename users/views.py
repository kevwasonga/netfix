from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import CustomerRegistrationForm
from django.utils.timezone import now
from services.models import ServiceRequest, Service

@login_required
def profile_view(request):
    user = request.user
    context = {}

    if user.is_customer:
        # Calculate age
        dob = user.customer_profile.date_of_birth
        user_age = now().year - dob.year - ((now().month, now().day) < (dob.month, dob.day))
        context['user_age'] = user_age

        # Fetch services requested by the customer
        context['sh'] = ServiceRequest.objects.filter(customer=user.customer_profile)
    elif user.is_company:
        # Fetch services provided by the company
        context['services'] = Service.objects.filter(company=user.company_profile)

    return render(request, 'users/profile.html', context)
def register_view(request):
    return render(request, 'users/register.html')



def register_customer(request):
    if request.method == 'POST':
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login after successful registration
    else:
        form = CustomerRegistrationForm()
    return render(request, 'users/register_customer.html', {'form': form})

from .forms import CompanyRegistrationForm

def register_company(request):
    if request.method == 'POST':
        form = CompanyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CompanyRegistrationForm()
    return render(request, 'users/register_company.html', {'form': form})




from django.shortcuts import render
from django.contrib.auth.decorators import login_required


