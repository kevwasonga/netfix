from django.shortcuts import render
from django.contrib.auth import logout as django_logout

from django.shortcuts import render
from django.db.models import Count
from services.models import RequestService  # Import your model


def home(request):
    # Fetch the top 5 most requested services
    top_services = (
        RequestService.objects.values('service__id', 'service__name', 'service__field','service__company__user__email')
        .annotate(request_count=Count('service'))
        .order_by('-request_count')[:5]
    )

    # Determine if the user is allowed to request a service (only customers)
    is_customer = request.user.is_authenticated and getattr(request.user, 'is_customer', False)

    return render(request, 'main/home.html', {
        'top_services': top_services,
        'is_customer': is_customer  # Pass user type to the template
    })


def logout(request):
    django_logout(request)
    return render(request, "main/logout.html")
