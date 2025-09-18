
from django import forms
from .models import Trip, Transportation_stretch


#from https://docs.djangoproject.com/en/3.0/topics/class-based-views/generic-editing/#model-forms
class DateForm(forms.ModelForm):
    class Meta:
        model = Trip
        fields = ['location', 'start_date', 'end_date', 'companion', 'emergency_contact', 'transportation', 'lodging', 'attractions', 'notes']
        widgets = {
            'start_date': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    'placeholder': 'Select a date',
                    'type': 'date'
                }
            ),
            'end_date': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    'placeholder': 'Select a date',
                    'type': 'date'
                }
            ),
        }

class TransportationForm:
    model = Transportation_stretch
    fields = all
