from django.contrib import admin
from .models import StudentProfile

class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'university', 'course', 'is_verified']
    list_filter = ['is_verified']
    list_editable = ['is_verified']
    readonly_fields = ['user', 'university', 'course', 'year_of_study', 'bio']

    def view_student_id(self, obj):
        if obj.student_id_document:
            return f'<a href="{obj.student_id_document.url}" target="_blank">View Document</a>'
        return 'No document'
    view_student_id.allow_tags = True

admin.site.register(StudentProfile, StudentProfileAdmin)