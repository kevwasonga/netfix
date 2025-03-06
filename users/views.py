from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views.generic import CreateView,DetailView, TemplateView

from .forms import CustomerSignUpForm, CompanySignUpForm, UserLoginForm
from .models import User, Company, Customer
from django.urls import reverse_lazy
from users.models import User, Company
from services.models import Service

from django.contrib.auth.views import LoginView
from services.models import RequestService



def register(request):
    return render(request, 'users/register.html')


class CustomerSignUpView(CreateView):
    model = User
    form_class = CustomerSignUpForm
    template_name = 'users/register_customer.html'
    success_url = "/" 



    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'customer'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        user.backend = "django.contrib.auth.backends.ModelBackend"  
        login(self.request, user, backend=user.backend)  
        return super().form_valid(form)

class CompanySignUpView(CreateView):
    model = User
    form_class = CompanySignUpForm
    template_name = 'users/register_company.html'
    success_url = "/" 


    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'company'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        user.backend = "django.contrib.auth.backends.ModelBackend"  # ✅ Set backend explicitly
        login(self.request, user, backend=user.backend)  # ✅ Login user with backend
        return super().form_valid(form)


class CustomLoginView(LoginView):
    template_name = "users/login.html"  
    authentication_form = UserLoginForm  

    def get_success_url(self):
     return "/"
    
    def form_invalid(self, form):
        # Add custom logic for failed login attempts
        form.add_error(None, "Invalid email, username or password.")
        return self.render_to_response(self.get_context_data(form=form))


# this view show the profile of individual users via url (example) http://127.0.0.1:8000/register/profile/1/
class UserProfileView(DetailView):
    model = Customer
    template_name = "users/profile.html"  # Create this template
    context_object_name = "user"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["service_requests"] = RequestService.objects.filter(customer=self.object)
        return context



