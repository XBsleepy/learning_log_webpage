from django.db import models
from django.utils import timezone
# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(default=timezone.now, blank=True, null=True)
    owner = models.ForeignKey('auth.User', related_name='tasks', on_delete=models.CASCADE)
    is_important = models.BooleanField(default=False)
    is_urgent = models.BooleanField(default=False)
    notice = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.title
    