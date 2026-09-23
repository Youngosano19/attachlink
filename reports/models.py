from django.db import models
from accounts.models import CustomUser
from attachments.models import Application

class WeeklyReport(models.Model):
    application = models.ForeignKey(Application, on_delete=models.CASCADE, related_name='weekly_reports')
    week_number = models.IntegerField()
    tasks_done = models.TextField()
    challenges = models.TextField(blank=True)
    next_week_plan = models.TextField(blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Week {self.week_number} - {self.application.student.username}"


class SupervisorFeedback(models.Model):
    report = models.OneToOneField(WeeklyReport, on_delete=models.CASCADE, related_name='feedback')
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    comment = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback for {self.report}"


class Task(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]

    application = models.ForeignKey(Application, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='pending')
    due_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.application.student.username}"