from django.shortcuts import render

def home(request):
    return render(request, 'esg_dashboard/home.html')

# Create your views here.
