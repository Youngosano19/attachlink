from django.urls import path
from . import views

urlpatterns = [
    path('submit/', views.submit_report, name='submit_report'),
    path('my-reports/', views.my_reports, name='my_reports'),
    path('my-tasks/', views.my_tasks, name='my_tasks'),
    path('view/<int:application_id>/', views.view_reports, name='view_reports'),
    path('feedback/<int:report_id>/', views.give_feedback, name='give_feedback'),
    path('assign-task/<int:application_id>/', views.assign_task, name='assign_task'),
]