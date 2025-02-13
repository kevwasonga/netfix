from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import register, register_customer, register_company, user_profile

urlpatterns = [
    path("register/", register, name="register"),
    path("register/customer/", register_customer, name="register_customer"),
    path("register/company/", register_company, name="register_company"),
    path("profile/", user_profile, name="user_profile"),
    
    # ✅ Login & Logout URLs
    path("login/", LoginView.as_view(template_name="users/login.html"), name="login"),
    path("logout/", LogoutView.as_view(next_page="/"), name="logout"),
]
