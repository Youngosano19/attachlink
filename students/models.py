from django.db import models
from accounts.models import CustomUser

class StudentProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='student_profile')
    university = models.CharField(max_length=200)
    course = models.CharField(max_length=200)
    year_of_study = models.IntegerField()
    cv = models.FileField(upload_to='cvs/', blank=True, null=True)
    student_id_document = models.FileField(upload_to='student_ids/', blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    bio = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - Student Profile"