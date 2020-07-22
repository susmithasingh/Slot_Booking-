from django.db import models

class Issues(models.Model):
    issue = models.TextField()
    reported_date_time = models.DateTimeField(auto_now=True)
    is_resolved = models.BooleanField(default=False)
