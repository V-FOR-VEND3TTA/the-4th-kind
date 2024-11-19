from django.shortcuts import render
from django.http import HttpResponseNotFound
from .models import TeamMember

def index(request):
    team_members = TeamMember.objects.all()
    return render(request, 'website/index.html', {'team_members': team_members})

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

def ts_and_cs(request):
    return render(request, 'website/terms-and-conditions.html')

def privacy_policy(request):
    return render(request, 'website/privacy-policy.html')
