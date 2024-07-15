from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class DairyItem(models.Model):
    """日记项"""
    topic = models.CharField(max_length=40, default='无题')
    text = models.TextField()
    date_added = models.DateTimeField(default=timezone.now, null=True, blank=True)
    today_score = models.IntegerField(default=60, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        """返回模型的字符串表示"""
        return self.text
