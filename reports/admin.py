from django.contrib import admin
from .models import WeeklyReport, Task, SupervisorFeedback

admin.site.register(WeeklyReport)
admin.site.register(Task)
admin.site.register(SupervisorFeedback)