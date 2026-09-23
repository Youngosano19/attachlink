from django.db import models
from accounts.models import CustomUser
from companies.models import CompanyProfile

class AttachmentPosition(models.Model):
    STATUS_CHOICES = [
        ('open', 'Open'),
        ('closed', 'Closed'),
    ]

    company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE, related_name='positions')
    title = models.CharField(max_length=200)
    department = models.CharField(max_length=100)
    description = models.TextField()
    requirements = models.TextField()
    duration = models.CharField(max_length=100, default='TBD')
    slots = models.IntegerField(default=1)
    location = models.CharField(max_length=200)
    slots = models.IntegerField(default=1)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='open')
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.title} - {self.company.company_name}"


class Application(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    student = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='applications')
    position = models.ForeignKey(AttachmentPosition, on_delete=models.CASCADE, related_name='applications')
    cover_letter = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    applied_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('student', 'position')

    def __str__(self):
        return f"{self.student.username} → {self.position.title}"