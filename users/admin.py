from django.contrib import admin
from .models import CustomUser, CustomerProfile, CompanyProfile

admin.site.register(CustomUser)
admin.site.register(CustomerProfile)
admin.site.register(CompanyProfile)
