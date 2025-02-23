from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, authenticate
from django.db import transaction
from django.core.exceptions import ValidationError

from .models import User, Company, Customer


class DateInput(forms.DateInput):
    input_type = 'date'


def validate_email(value):
    # In case the email already exists in an email input in a registration form, this function is fired
    if User.objects.filter(email=value).exists():
        raise ValidationError(
            value + " is already taken.")

class CustomerSignUpForm(UserCreationForm):
    username = forms.CharField(max_length=150, required=True, widget=forms.TextInput(
        attrs={'placeholder': 'Enter Username'}))
    email = forms.EmailField(required=True, validators=[validate_email], widget=forms.EmailInput(
        attrs={'placeholder': 'Enter Email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Enter Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Confirm Password'}))
    date_of_birth = forms.DateField(required=True, widget=DateInput())

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2", "date_of_birth"]

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_customer = True
        if commit:
            user.save()
            Customer.objects.create(user=user)
        return user


class CompanySignUpForm(UserCreationForm):
    username = forms.CharField(max_length=150, required=True, widget=forms.TextInput(
        attrs={'placeholder': 'Enter Username'}))
    email = forms.EmailField(required=True, validators=[validate_email], widget=forms.EmailInput(
        attrs={'placeholder': 'Enter Email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Enter Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Confirm Password'}))
    
    # Change to ChoiceField to match model field
    field_of_work = forms.ChoiceField(
        choices=Company._meta.get_field('field_of_work').choices,
        required=True
    )

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2", "field_of_work"]

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_company = True  # Mark as a company
        if commit:
            user.save()
            # ✅ Create the Company object linked to the user
            Company.objects.create(user=user, field_of_work=self.cleaned_data['field_of_work'])
        return user



class UserLoginForm(AuthenticationForm):  # Inherit from AuthenticationForm
    email = forms.EmailField(widget=forms.TextInput(
        attrs={'placeholder': 'Enter Email', 'autocomplete': 'off'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password'}))
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['autocomplete'] = 'off'