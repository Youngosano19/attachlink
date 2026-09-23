from django.urls import path
from . import views

urlpatterns = [
    path('', views.browse_positions, name='browse_positions'),
    path('post/', views.post_position, name='post_position'),
    path('<int:pk>/', views.position_detail, name='position_detail'),
    path('<int:pk>/apply/', views.apply_position, name='apply_position'),
    path('<int:pk>/applicants/', views.view_applicants, name='view_applicants'),
    path('application/<int:pk>/<str:status>/', views.update_application, name='update_application'),
]