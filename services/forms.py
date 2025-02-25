from django import forms
from .models import RequestService
from .models import Company, Service
from users.forms import  CompanySignUpForm


class CreateNewService(forms.Form):
    name = forms.CharField(max_length=40)
    description = forms.CharField(widget=forms.Textarea, label='Description')
    price_hour = forms.DecimalField(
    decimal_places=2, max_digits=5, min_value=0.00)
    field = forms.ChoiceField(choices=Service.choices, required=True)  

    def __init__(self, *args, choices='', ** kwargs):
        super(CreateNewService, self).__init__(*args, **kwargs)
        # adding choices to fields
        if choices:
            self.fields['field'].choices = choices
        # adding placeholders to form fields
        self.fields['name'].widget.attrs['placeholder'] = 'Enter Service Name'
        self.fields['description'].widget.attrs['placeholder'] = 'Enter Description'
        self.fields['price_hour'].widget.attrs['placeholder'] = 'Enter Price per Hour'

        self.fields['name'].widget.attrs['autocomplete'] = 'off'





class RequestServiceForm(forms.ModelForm):
    class Meta:
        model = RequestService
        fields = ['address', 'hours']
        widgets = {
            'address': forms.Textarea(attrs={'placeholder': 'Enter Address', 'rows': 2}),
            'hours': forms.NumberInput(attrs={'min': 1}),
        }

