from django.shortcuts import render
from django.http import HttpResponseNotFound

def index(request):
    return render(request, 'website/index.html')

def about(request):
    return render(request, 'website/about.html')

def contact(request):
    return render(request, 'website/contact.html')

def case_studies(request):
    return render(request, 'website/case-studies.html')

def services(request):
    return render(request, 'website/services.html')

def team(request):
    return render(request, 'website/team.html')

def custom_404(request, exception):
    return render(request, 'website/404.html', status=404)
