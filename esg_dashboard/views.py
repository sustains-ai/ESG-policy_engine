from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, 'esg_dashboard/home.html')

# Create your views here.
