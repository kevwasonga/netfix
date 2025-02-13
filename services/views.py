from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt
from .models import Service, CompanyProfile

def field_services_view(request, field):
    """ Displays all services in a specific field (e.g., Plumbing, Housekeeping) """
    services = Service.objects.filter(field=field)
    context = {
        'field': field,
        'services': services,
    }
    return render(request, 'services/field.html', context)

def services_list_view(request):
    """ Displays a list of all available services """
    services = Service.objects.all()
    context = {
        'services': services,
    }
    return render(request, 'services/list.html', context)

@csrf_exempt
def request_service_view(request, id):
    """ Allows a customer to request a service """
    service = get_object_or_404(Service, id=id)
    if request.method == 'POST':
        # Process the service request (e.g., save it to the database)
        return redirect('/services/')  # Redirect to services list after submission
    return render(request, 'services/request_service.html', {'service': service})

def single_service_view(request, id):
    """ Displays details of a single service, including the company offering it """
    service = get_object_or_404(Service, id=id)
    company = service.company  # Fetch the company offering this service
    return render(request, 'services/single_service.html', {
        'service': service,
        'company': company,
    })
