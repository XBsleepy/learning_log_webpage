from django import forms
from .models import Task
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'due_date', 'is_important', 'is_urgent', 'notice']
        labels = {'title': 'Task', 'due_date': 'Due Date', 'is_important': 'Important', 'is_urgent': 'Urgent', 'notice': 'Notice'}
        widgets = {'notice': forms.Textarea(attrs={'cols': 80})}
