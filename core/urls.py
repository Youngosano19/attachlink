from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import admin_views
from django.shortcuts import render

def home(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'home.html')

from django.shortcuts import redirect

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('students/', include('students.urls')),
    path('companies/', include('companies.urls')),
    path('positions/', include('attachments.urls')),
    path('reports/', include('reports.urls')),
    path('admin-dashboard/', admin_views.admin_dashboard, name='admin_dashboard'),
    path('admin-dashboard/approve-company/<int:pk>/', admin_views.approve_company, name='approve_company'),
    path('admin-dashboard/deactivate-user/<int:pk>/', admin_views.deactivate_user, name='deactivate_user'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)