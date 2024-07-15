from django import forms
from .models import DairyItem

class DairyItemForm(forms.ModelForm):
    class Meta:
        model = DairyItem
        fields = ['topic', 'text', 'today_score', 'date_added']
        widgets = {
            'topic': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'cols': 80, 'rows': 10, 'class': 'form-control'}),
            'today_score': forms.NumberInput(attrs={'class': 'form-control'}),
            'date_added': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
        }
