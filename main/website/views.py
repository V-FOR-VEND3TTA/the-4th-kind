from django.shortcuts import render
from django.http import HttpResponseNotFound
from .models import TeamMember

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

def team_view(request):
    team_members = TeamMember.objects.all()
    return render(request, 'team.html', {'team_members': team_members})

def custom_404(request, exception):
    return render(request, 'website/404.html', status=404)
