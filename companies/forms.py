from django import forms
from .models import CompanyProfile

class CompanyProfileForm(forms.ModelForm):
    class Meta:
        model = CompanyProfile
        fields = ['company_name', 'industry', 'location', 'website', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }