from django import forms
from .models import AttachmentPosition, Application

class PositionForm(forms.ModelForm):
    class Meta:
        model = AttachmentPosition
        fields = ['title', 'department', 'duration', 'location', 'slots', 'requirements', 'description']
        widgets = {
            'requirements': forms.Textarea(attrs={'rows': 3}),
            'description': forms.Textarea(attrs={'rows': 3}),
        }

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['cover_letter']
        widgets = {
            'cover_letter': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Write a brief cover letter...'}),
        }