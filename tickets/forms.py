from django import forms
from .models import Ticket, Sample

# Ticket Form
class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['traffic', 'category', 'description']  # Include fields you want to show

        # Customizing the widgets and labels (optional)
        widgets = {
            'traffic': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }

        labels = {
            'traffic': 'Traffic Direction',
            'category': 'Category',
            'description': 'Description of the Issue',
        }

# Sample Form
class SampleForm(forms.ModelForm):
    class Meta:
        model = Sample
        fields = ['timestamp', 'calling_number', 'called_number']

        # Customizing the widgets and labels (optional)
        widgets = {
            'timestamp': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'calling_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'called_number': forms.NumberInput(attrs={'class': 'form-control'}),
        }

        labels = {
            'timestamp': 'Timestamp',
            'calling_number': 'Calling Number',
            'called_number': 'Called Number',
        }
