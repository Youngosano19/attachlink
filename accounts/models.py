from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    STUDENT = 'student'
    COMPANY = 'company'
    ADMIN = 'admin'

    ROLE_CHOICES = [
        (STUDENT, 'Student'),
        (COMPANY, 'Company Staff'),
        (ADMIN, 'Admin'),
    ]

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=STUDENT)
    phone = models.CharField(max_length=20, blank=True)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)

    def is_student(self):
        return self.role == self.STUDENT

    def is_company(self):
        return self.role == self.COMPANY

    def is_admin_user(self):
        return self.role == self.ADMIN

    def __str__(self):
        return f"{self.username} ({self.role})"