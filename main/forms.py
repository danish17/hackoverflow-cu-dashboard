from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'venue', 'date', 'time', 'img']
        labels = {
            'name': 'What is the event called?*',
            'venue': 'Where is the event going to be held?*',
            'date': 'When is the event scheduled?*',
            'time': 'At what time?*',
            'img': 'Event Image*',
        }
        help_texts = {
            'date': '(YYYY-MM-DD)',
            'time': '(HH:MM 24 Hour)',
        }