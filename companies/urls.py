from django.urls import path
from . import views

urlpatterns = [
    path('setup/', views.setup_company, name='setup_company'),
    path('dashboard/', views.company_dashboard, name='company_dashboard'),
    path('profile/', views.edit_company_profile, name='edit_company_profile'),
    path('applicants/', views.all_applicants, name='all_applicants'),
]