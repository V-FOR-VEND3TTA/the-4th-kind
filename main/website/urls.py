from django.urls import path
from website import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('case-studies/', views.case_studies, name='case-studies'),
    path('services/', views.services, name='services'),
    path('team/', views.team, name='team'),
    path('terms-and-conditions/', views.ts_and_cs, name='terms-and-conditions'),
    path('privacy-policy/', views.privacy_policy, name='privacy-policy'),
]
