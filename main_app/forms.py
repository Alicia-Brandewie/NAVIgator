
from django import forms
from .models import Trip


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
        # widgets = {
        #     'end_date': forms.DateInput(
        #         format=('%Y-%m-%d'),
        #         attrs={
        #             'placeholder': 'Select a date',
        #             'type': 'date'
        #         }
        #     ),
        # }




# from https://forum.djangoproject.com/t/changing-input-type-in-a-class-based-create-view/2334
    # class DateInput(forms.DateInput):
    #     # Subclass of Django’s DateInput widget to use <input type=date>.
    #     input_type = 'start_date'
    # def customize_fields(db_field, **kwargs):
    #     if isinstance(db_field, models.DateField):
    #         kwargs["widget"] = DateInput
    #     return db_field.formfield(**kwargs)
    # class TripForm(forms.ModelForm):
    #     class Meta:
    #         model = Trip
    #         fields = ['location', 'start_date', 'end_date', 'companion', 'emergency_contact', 'transportation', 'lodging', 'attractions', 'notes']
    #         formfield_callback = customize_fields
