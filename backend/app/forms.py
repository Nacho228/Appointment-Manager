from django import forms
from .models import Appointment

class UpdateAppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['service', 'day', 'time']