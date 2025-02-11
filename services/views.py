from django.shortcuts import render
from .models import Service

def field_services_view(request, field):
    services = Service.objects.filter(field=field)
    context = {
        'field': field,
        'services': services,
    }
    return render(request, 'services/field.html', context)

def services_list_view(request):
    services = Service.objects.all()
    context = {
        'services': services,
    }
    return render(request, 'services/list.html', context)


from django.shortcuts import get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def request_service_view(request, id):
    service = get_object_or_404(Service, id=id)
    if request.method == 'POST':
        # Process the service request (e.g., save it to the database)
        return redirect('/services/')  # Redirect to services list after submission
    return render(request, 'services/request_service.html', {'service': service})

def single_service_view(request, id):
    service = get_object_or_404(Service, id=id)
    return render(request, 'services/single_service.html', {'service': service})
