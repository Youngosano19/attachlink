from django.shortcuts import render, redirect
from django.contrib import messages
from .models import StudentProfile
from .forms import StudentProfileForm
from accounts.decorators import student_required

@student_required
def setup_profile(request):
    try:
        profile = request.user.student_profile
        return redirect('student_dashboard')
    except StudentProfile.DoesNotExist:
        pass

    if request.method == 'POST':
        form = StudentProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('student_dashboard')
    else:
        form = StudentProfileForm()
    return render(request, 'students/setup_profile.html', {'form': form})

@student_required
def student_dashboard(request):
    try:
        profile = request.user.student_profile
    except StudentProfile.DoesNotExist:
        return redirect('setup_profile')

    applications = request.user.applications.all()
    return render(request, 'students/dashboard.html', {
        'profile': profile,
        'applications': applications,
    })
@student_required
def edit_profile(request):
    try:
        profile = request.user.student_profile
    except StudentProfile.DoesNotExist:
        return redirect('setup_profile')

    if request.method == 'POST':
        form = StudentProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('edit_profile')
    else:
        form = StudentProfileForm(instance=profile)
    return render(request, 'students/edit_profile.html', {
        'form': form,
        'profile': profile,
    })