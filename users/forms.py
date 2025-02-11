from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, CustomerProfile, CompanyProfile, FIELD_OF_WORK_CHOICES

# Form for customer registration
class CustomerRegistrationForm(UserCreationForm):
    date_of_birth = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        required=True,
        label="Date of Birth"
    )

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'date_of_birth']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_customer = True  # Mark the user as a customer
        if commit:
            user.save()
            # Create the associated customer profile
            CustomerProfile.objects.create(
                user=user,
                date_of_birth=self.cleaned_data['date_of_birth']
            )
        return user

# Form for company registration
class CompanyRegistrationForm(UserCreationForm):
    field_of_work = forms.ChoiceField(
        choices=FIELD_OF_WORK_CHOICES,
        required=True,
        label="Field of Work"
    )

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'field_of_work']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_company = True  # Mark the user as a company
        if commit:
            user.save()
            # Create the associated company profile
            CompanyProfile.objects.create(
                user=user,
                field_of_work=self.cleaned_data['field_of_work']
            )
        return user
