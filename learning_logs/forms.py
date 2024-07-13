from django import forms

from .models import Topic, Entry


from django import forms
from .models import Topic

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text', 'topic_aim']
        labels = {'text': 'Topic', 'topic_aim': 'Goal'}
        widgets = {
            'text': forms.TextInput(attrs={'class': 'form-control'}),
            'topic_aim': forms.TextInput(attrs={'class': 'form-control'}),
        }



class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}