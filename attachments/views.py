from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import AttachmentPosition, Application
from .forms import PositionForm, ApplicationForm

@login_required
def browse_positions(request):
    positions = AttachmentPosition.objects.filter(status='open')
    return render(request, 'attachments/browse.html', {'positions': positions})

@login_required
def post_position(request):
    try:
        company = request.user.company_profile
    except:
        return redirect('setup_company')

    if request.method == 'POST':
        form = PositionForm(request.POST)
        if form.is_valid():
            position = form.save(commit=False)
            position.company = company
            position.save()
            return redirect('company_dashboard')
    else:
        form = PositionForm()
    return render(request, 'attachments/post_position.html', {'form': form})

@login_required
def position_detail(request, pk):
    position = get_object_or_404(AttachmentPosition, pk=pk)
    already_applied = False
    if request.user.is_authenticated:
        already_applied = Application.objects.filter(
            student=request.user, position=position
        ).exists()
    return render(request, 'attachments/position_detail.html', {
        'position': position,
        'already_applied': already_applied,
    })

@login_required
def apply_position(request, pk):
    position = get_object_or_404(AttachmentPosition, pk=pk)

    # Check student is verified
    try:
        if not request.user.student_profile.is_verified:
            return render(request, 'attachments/not_verified.html')
    except:
        pass

    if Application.objects.filter(student=request.user, position=position).exists():
        return redirect('position_detail', pk=pk)

    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.student = request.user
            application.position = position
            application.save()
            return redirect('student_dashboard')
    else:
        form = ApplicationForm()
    return render(request, 'attachments/apply.html', {'form': form, 'position': position})

@login_required
def view_applicants(request, pk):
    position = get_object_or_404(AttachmentPosition, pk=pk)
    applications = position.applications.all()
    return render(request, 'attachments/applicants.html', {
        'position': position,
        'applications': applications,
    })

@login_required
def update_application(request, pk, status):
    application = get_object_or_404(Application, pk=pk)
    if status in ['approved', 'rejected']:
        application.status = status
        application.save()
    return redirect('view_applicants', pk=application.position.pk)