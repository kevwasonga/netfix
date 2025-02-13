from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, CustomerProfile, CompanyProfile, FIELD_OF_WORK_CHOICES

# ✅ Customer Registration Form
class CustomerRegistrationForm(UserCreationForm):
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_customer = True
        if commit:
            user.save()
            CustomerProfile.objects.create(user=user, date_of_birth=self.cleaned_data["date_of_birth"])
        return user

# ✅ Company Registration Form
class CompanyRegistrationForm(UserCreationForm):
    field_of_work = forms.ChoiceField(choices=FIELD_OF_WORK_CHOICES)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'field_of_work']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_company = True
        if commit:
            user.save()
            CompanyProfile.objects.create(user=user, field_of_work=self.cleaned_data["field_of_work"])
        return user
