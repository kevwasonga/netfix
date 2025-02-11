from django.db import models
from django.conf import settings  # Import for AUTH_USER_MODEL


class CompanyProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Use AUTH_USER_MODEL
    field_of_work = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username


class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price_hour = models.DecimalField(max_digits=10, decimal_places=2)
    field = models.CharField(max_length=100)
    company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE, related_name='services')

    def __str__(self):
        return self.name


class ServiceRequest(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    customer = models.ForeignKey('users.CustomerProfile', on_delete=models.CASCADE)  # Lazy reference to avoid circular imports
    address = models.TextField()
    hours = models.PositiveIntegerField()
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    requested_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Request by {self.customer.user.username} for {self.service.name}"
