from django.contrib.auth.models import AbstractUser
from django.db import models

# ✅ Choices for company field of work
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

# ✅ Custom User Model
class CustomUser(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_company = models.BooleanField(default=False)

    # ✅ Fix reverse accessor clashes
    groups = models.ManyToManyField(
        "auth.Group",
        related_name="customuser_groups",  # Unique related_name
        blank=True
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="customuser_permissions",  # Unique related_name
        blank=True
    )

    def __str__(self):
        return self.username


# ✅ Customer Profile Model
class CustomerProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="customer_profile")
    date_of_birth = models.DateField()

    def __str__(self):
        return f"Customer: {self.user.username}"

# ✅ Company Profile Model
class CompanyProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="company_profile")
    field_of_work = models.CharField(max_length=50, choices=FIELD_OF_WORK_CHOICES)

    def __str__(self):
        return f"Company: {self.user.username} ({self.field_of_work})"
