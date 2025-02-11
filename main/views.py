from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# View for the home page
def home_view(request):
    return render(request, 'main/home.html')

# View for the logout page
#@login_required
def logout_view(request):
    return render(request, 'main/logout.html')
