from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class dairy_item(models.Model):
    """A dairy item."""
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    mood_choices = (
        ('happy', 'Happy'),
        ('sad', 'Sad'),
        ('angry', 'Angry'),
        ('neutral', 'Neutral'),
    )
    mood = models.CharField(max_length=10, choices=mood_choices, default='neutral')
    today_score = models.IntegerField(default=60, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        """Return a string representation of the model."""
        return self.text