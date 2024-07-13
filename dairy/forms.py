from django import forms
from .models import dairy_item

class DairyItemForm(forms.ModelForm):
    class Meta:
        model = dairy_item
        fields = ['text', 'mood', 'today_score']
        labels = {'text': 'Dairy Item', 'mood': 'Mood', 'today_score': 'Today Score'}
        widgets = {
            'text': forms.Textarea(attrs={'cols': 80}),
            'mood': forms.Select(attrs={'class': 'form-control'}),
            'today_score': forms.NumberInput(attrs={'class': 'form-control'}),
        }