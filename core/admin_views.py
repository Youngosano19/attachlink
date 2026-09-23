from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Count
from django.db.models.functions import TruncMonth
from accounts.models import CustomUser
from companies.models import CompanyProfile
from attachments.models import AttachmentPosition, Application
from reports.models import WeeklyReport, SupervisorFeedback
import json
from datetime import datetime

@staff_member_required
def admin_dashboard(request):
    # Core stats
    total_students = CustomUser.objects.filter(role='student').count()
    total_companies = CustomUser.objects.filter(role='company').count()
    total_positions = AttachmentPosition.objects.count()
    total_applications = Application.objects.count()
    total_reports = WeeklyReport.objects.count()
    pending_companies = CompanyProfile.objects.filter(is_approved=False).count()
    approved_applications = Application.objects.filter(status='approved').count()
    rejected_applications = Application.objects.filter(status='rejected').count()
    pending_applications = Application.objects.filter(status='pending').count()

    # Applications by status for pie chart
    app_status_data = {
        'labels': ['Approved', 'Pending', 'Rejected'],
        'data': [approved_applications, pending_applications, rejected_applications],
        'colors': ['#28a745', '#ffc107', '#dc3545'],
    }

    # Monthly registrations for line chart
    monthly_students = (
        CustomUser.objects.filter(role='student')
        .annotate(month=TruncMonth('date_joined'))
        .values('month')
        .annotate(count=Count('id'))
        .order_by('month')[:6]
    )
    monthly_companies = (
        CustomUser.objects.filter(role='company')
        .annotate(month=TruncMonth('date_joined'))
        .values('month')
        .annotate(count=Count('id'))
        .order_by('month')[:6]
    )

    student_months = [entry['month'].strftime('%b %Y') for entry in monthly_students]
    student_counts = [entry['count'] for entry in monthly_students]
    company_months = [entry['month'].strftime('%b %Y') for entry in monthly_companies]
    company_counts = [entry['count'] for entry in monthly_companies]

    registration_data = {
        'labels': student_months,
        'students': student_counts,
        'companies': company_counts,
    }

    # Top companies by applicants
    top_companies = (
        CompanyProfile.objects
        .annotate(app_count=Count('positions__applications'))
        .order_by('-app_count')[:5]
    )
    top_companies_data = {
        'labels': [c.company_name for c in top_companies],
        'data': [c.app_count for c in top_companies],
    }

    # Recent data
    recent_users = CustomUser.objects.order_by('-date_joined')[:5]
    recent_applications = Application.objects.order_by('-applied_at')[:5]
    pending_company_list = CompanyProfile.objects.filter(is_approved=False)

    return render(request, 'admin_dashboard.html', {
        'total_students': total_students,
        'total_companies': total_companies,
        'total_positions': total_positions,
        'total_applications': total_applications,
        'total_reports': total_reports,
        'pending_companies': pending_companies,
        'approved_applications': approved_applications,
        'recent_users': recent_users,
        'recent_applications': recent_applications,
        'pending_company_list': pending_company_list,
        'app_status_data': json.dumps(app_status_data),
        'registration_data': json.dumps(registration_data),
        'top_companies_data': json.dumps(top_companies_data),
    })

@staff_member_required
def approve_company(request, pk):
    company = get_object_or_404(CompanyProfile, pk=pk)
    company.is_approved = True
    company.save()
    return redirect('admin_dashboard')

@staff_member_required
def deactivate_user(request, pk):
    user = get_object_or_404(CustomUser, pk=pk)
    user.is_active = False
    user.save()
    return redirect('admin_dashboard')