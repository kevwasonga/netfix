from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.signals import post_save
from django.dispatch import receiver

class User(AbstractUser):
    email = models.EmailField(unique=True)  
    is_company = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'  
    REQUIRED_FIELDS = ['username']  

    def __str__(self):
        return self.email


class Customer(models.Model):
    user = models.OneToOneField('users.User', on_delete=models.CASCADE, primary_key=True)
    date_of_birth = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.email


class Company(models.Model):
    user = models.OneToOneField('users.User', on_delete=models.CASCADE, primary_key=True)
    field_of_work = models.CharField(
        max_length=70,
        choices=[
            ('Air Conditioner', 'Air Conditioner'),
            ('All in One', 'All in One'),
            ('Carpentry', 'Carpentry'),
            ('Electricity', 'Electricity'),
            ('Gardening', 'Gardening'),
            ('Home Machines', 'Home Machines'),
            ('House Keeping', 'House Keeping'),
            ('Interior Design', 'Interior Design'),
            ('Locks', 'Locks'),
            ('Painting', 'Painting'),
            ('Plumbing', 'Plumbing'),
            ('Water Heaters', 'Water Heaters')
        ],
        blank=False, null=False
    )
    rating = models.IntegerField(
        validators=[MaxValueValidator(5), MinValueValidator(0)], default=0
    )

    def __str__(self):
        return self.user.email  # Ensure email is used for consistency


# ✅ Automatically set `is_company = True` when a Company is created
@receiver(post_save, sender=Company)
def mark_user_as_company(sender, instance, created, **kwargs):
    if created:
        instance.user.is_company = True
        instance.user.save()
