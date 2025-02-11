from django.contrib.auth.models import AbstractUser
from django.db import models

# Choices for the field of work
FIELD_OF_WORK_CHOICES = [
    ("Air Conditioner", "Air Conditioner"),
    ("Carpentry", "Carpentry"),
    ("Electricity", "Electricity"),
    ("Gardening", "Gardening"),
    ("Home Machines", "Home Machines"),
    ("Housekeeping", "Housekeeping"),
    ("Interior Design", "Interior Design"),
    ("Locks", "Locks"),
    ("Painting", "Painting"),
    ("Plumbing", "Plumbing"),
    ("Water Heaters", "Water Heaters"),
    ("All in One", "All in One"),
]

# Custom user model


# Custom user model
class CustomUser(AbstractUser):
    """
    Custom user model that extends AbstractUser and adds fields to differentiate between user types.
    """
    is_customer = models.BooleanField(default=False)
    is_company = models.BooleanField(default=False)

    # Override groups and user_permissions to provide unique related_name attributes
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_groups',  # Use a unique related_name
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_user_permissions',  # Use a unique related_name
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    def __str__(self):
        return self.username


# Customer profile model
class CustomerProfile(models.Model):
    """
    Stores additional information specific to customers.
    """
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='customer_profile')
    date_of_birth = models.DateField()

    def __str__(self):
        return f"Customer: {self.user.username}"

# Company profile model
class CompanyProfile(models.Model):
    """
    Stores additional information specific to companies, including their field of work.
    """
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='company_profile')
    field_of_work = models.CharField(max_length=50, choices=FIELD_OF_WORK_CHOICES)

    def __str__(self):
        return f"Company: {self.user.username} ({self.field_of_work})"
