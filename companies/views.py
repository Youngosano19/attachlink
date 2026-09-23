from django.shortcuts import render, redirect
from .models import CompanyProfile
from .forms import CompanyProfileForm
from accounts.decorators import company_required

@company_required
def setup_company(request):
    try:
        profile = request.user.company_profile
        return redirect('company_dashboard')
    except CompanyProfile.DoesNotExist:
        pass

    if request.method == 'POST':
        form = CompanyProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('company_dashboard')
    else:
        form = CompanyProfileForm()
    return render(request, 'companies/setup_company.html', {'form': form})

@company_required
def company_dashboard(request):
    try:
        profile = request.user.company_profile
    except CompanyProfile.DoesNotExist:
        return redirect('setup_company')

    positions = profile.positions.all()
    total_applicants = sum(p.applications.count() for p in positions)
    pending = sum(p.applications.filter(status='pending').count() for p in positions)
    approved = sum(p.applications.filter(status='approved').count() for p in positions)

    return render(request, 'companies/dashboard.html', {
        'profile': profile,
        'positions': positions,
        'total_applicants': total_applicants,
        'pending': pending,
        'approved': approved,
    })
@company_required
def edit_company_profile(request):
    try:
        profile = request.user.company_profile
    except CompanyProfile.DoesNotExist:
        return redirect('setup_company')

    if request.method == 'POST':
        form = CompanyProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('edit_company_profile')
    else:
        form = CompanyProfileForm(instance=profile)
    return render(request, 'companies/edit_profile.html', {
        'form': form,
        'profile': profile,
    })
@company_required
def all_applicants(request):
    try:
        profile = request.user.company_profile
    except CompanyProfile.DoesNotExist:
        return redirect('setup_company')
    
    positions = profile.positions.all()
    applications = []
    for position in positions:
        for app in position.applications.all():
            applications.append(app)
    
    return render(request, 'companies/all_applicants.html', {
        'applications': applications,
        'profile': profile,
    })