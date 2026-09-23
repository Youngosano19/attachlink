from django.urls import path
from . import views

urlpatterns = [
    path('setup/', views.setup_profile, name='setup_profile'),
    path('dashboard/', views.student_dashboard, name='student_dashboard'),
    path('profile/', views.edit_profile, name='edit_profile'),
]