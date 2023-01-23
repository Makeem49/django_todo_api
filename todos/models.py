from django.utils import timezone

from django.db import models

# Create your models here.

class Todo(models.Model):
    name = models.CharField(max_length=100, null=False)
    created_at = models.DateTimeField(null=False, default=timezone.now)
    target_time = models.TimeField( null=True)
    duration = models.TimeField(null=True, blank=True)
    start_at = models.TimeField(null=True, blank=True)
    completed_at = models.TimeField( null=True, blank=True)
    is_suspended = models.BooleanField(null=True, blank=True, default=False)
    is_completed = models.BooleanField(null=True, blank=True, default=False)

    def is_done(self):
        return self.is_completed

    @property
    def get_target_time(self):
        if self.target_time is None:
            return 'Target not set yet.'
        return self.target_time

