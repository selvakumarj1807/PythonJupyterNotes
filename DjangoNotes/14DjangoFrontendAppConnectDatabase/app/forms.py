# forms.py
from django import forms
from .models import Appoitment, Doctor

class AppoitmentForm(forms.ModelForm):
    department = forms.ChoiceField(choices=[], widget=forms.Select(attrs={
        'class': 'form-control'
    }))

    class Meta:
        model = Appoitment
        fields = ['name', 'email', 'contact', 'date', 'time', 'department']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone'}),
            'date': forms.TextInput(attrs={'class': 'form-control appointment_date', 'placeholder': 'Date'}),
            'time': forms.TextInput(attrs={'class': 'form-control appointment_time', 'placeholder': 'Time'}),
        }

    def __init__(self, *args, **kwargs):
        super(AppoitmentForm, self).__init__(*args, **kwargs)
        # Get unique positions from Doctor model
        positions = Doctor.objects.values_list('position', flat=True).distinct()
        choices = [(pos, pos) for pos in positions]
        # Add a default placeholder choice
        choices.insert(0, ('', 'Department'))
        self.fields['department'].choices = choices
