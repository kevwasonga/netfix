from django.contrib import admin
from .models import CustomUser, CustomerProfile, CompanyProfile

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "is_customer", "is_company", "is_staff")
    list_filter = ("is_customer", "is_company")
    search_fields = ("username", "email")

@admin.register(CustomerProfile)
class CustomerProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "date_of_birth")

@admin.register(CompanyProfile)
class CompanyProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "field_of_work")
    list_filter = ("field_of_work",)
