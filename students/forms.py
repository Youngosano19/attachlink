from django import forms
from .models import StudentProfile

def validate_pdf(value):
    if not value.name.endswith('.pdf'):
        raise forms.ValidationError('Only PDF files are allowed.')
    if value.size > 5 * 1024 * 1024:
        raise forms.ValidationError('File size must not exceed 5MB.')

class StudentProfileForm(forms.ModelForm):
    cv = forms.FileField(
        required=False,
        validators=[validate_pdf],
        widget=forms.FileInput(attrs={'accept': '.pdf'}),
        help_text='Upload your CV in PDF format only (max 5MB).'
    )
    student_id_document = forms.FileField(
        required=False,
        widget=forms.FileInput(attrs={'accept': '.pdf,.jpg,.jpeg,.png'}),
        help_text='Upload your student ID card or admission letter (PDF or image).'
    )

    class Meta:
        model = StudentProfile
        fields = ['university', 'course', 'year_of_study', 'cv', 'student_id_document', 'bio']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 3}),
        }