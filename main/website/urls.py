from django.urls import path
from website import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('case-studies/', views.case_studies, name='case-studies'),
    path('services/', views.services, name='services'),
    path('team/', views.team_view, name='team'),
]

handler404 = 'website.views.custom_404'
