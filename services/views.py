from django.shortcuts import render, redirect, get_object_or_404

from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from users.models import Company, Customer, User
from django.contrib import messages


from .models import Service
from .forms import CreateNewService, RequestServiceForm


def service_list(request):
    services = Service.objects.all().order_by("-date")
    return render(request, 'services/list.html', {'services': services})


def index(request, id):
    service = Service.objects.get(id=id)
    return render(request, 'services/single_service.html', {'service': service})

@login_required
def create(request):
    if request.method == "POST":
        form = CreateNewService(request.POST)
        if form.is_valid():
            # Get current logged-in company
            company = Company.objects.get(user=request.user)

            # Create new service
            Service.objects.create(
                company=company,
                name=form.cleaned_data['name'],
                description=form.cleaned_data['description'],
                price_hour=form.cleaned_data['price_hour'],
                field=form.cleaned_data['field'],
            )
            messages.success(request, "Service created successfully!")
            return redirect("service_list")  

    else:
        form = CreateNewService(choices=Service.choices)

    return render(request, "services/create.html", {"form": form})



def service_field(request, field):
    # search for the service present in the url
    field = field.replace('-', ' ').title()
    services = Service.objects.filter(
        field=field)
    return render(request, 'services/field.html', {'services': services, 'field': field})

@login_required
def request_service(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    
    if request.method == "POST":
        form = RequestServiceForm(request.POST)
        if form.is_valid():
            request_service = form.save(commit=False)
            request_service.customer = request.user
            request_service.service = service
            request_service.save()
            messages.success(request, "Service request submitted successfully!")
            return redirect("service_list")
    else:
        form = RequestServiceForm()

    return render(request, "services/request_service.html", {"form": form, "service": service})
