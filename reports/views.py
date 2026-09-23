from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import WeeklyReport, Task, SupervisorFeedback
from .forms import WeeklyReportForm, TaskForm, FeedbackForm
from attachments.models import Application

@login_required
def submit_report(request):
    try:
        applications = request.user.applications.filter(status='approved')
        if not applications.exists():
            return render(request, 'reports/no_application.html')
        application = applications.first()
    except:
        return redirect('student_dashboard')

    if request.method == 'POST':
        form = WeeklyReportForm(request.POST)
        if form.is_valid():
            report = form.save(commit=False)
            report.application = application
            report.save()
            return redirect('my_reports')
    else:
        form = WeeklyReportForm()
    return render(request, 'reports/submit_report.html', {'form': form, 'application': application})

@login_required
def my_reports(request):
    try:
        applications = request.user.applications.filter(status='approved')
        reports = WeeklyReport.objects.filter(application__in=applications).order_by('-submitted_at')
    except:
        reports = []
    return render(request, 'reports/my_reports.html', {'reports': reports})

@login_required
def my_tasks(request):
    try:
        applications = request.user.applications.filter(status='approved')
        tasks = Task.objects.filter(application__in=applications)
    except:
        tasks = []
    return render(request, 'reports/my_tasks.html', {'tasks': tasks})

@login_required
def view_reports(request, application_id):
    application = get_object_or_404(Application, pk=application_id)
    reports = application.weekly_reports.all().order_by('-submitted_at')
    return render(request, 'reports/view_reports.html', {
        'application': application,
        'reports': reports,
    })

@login_required
def give_feedback(request, report_id):
    report = get_object_or_404(WeeklyReport, pk=report_id)
    if hasattr(report, 'feedback'):
        return redirect('view_reports', application_id=report.application.pk)

    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.report = report
            feedback.supervisor = request.user
            feedback.save()
            return redirect('view_reports', application_id=report.application.pk)
    else:
        form = FeedbackForm()
    return render(request, 'reports/give_feedback.html', {'form': form, 'report': report})

@login_required
def assign_task(request, application_id):
    application = get_object_or_404(Application, pk=application_id)
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.application = application
            task.save()
            return redirect('view_reports', application_id=application_id)
    else:
        form = TaskForm()
    return render(request, 'reports/assign_task.html', {'form': form, 'application': application})