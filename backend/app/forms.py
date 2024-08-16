from rest_framework import serializers
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Appointment

class DateField(serializers.DateField):
    def to_representation(self, value):
        # Convert datetime to date for serialization
        return super().to_representation(value.date()) if value else None

# Custom date selector widget used for selecting dates
class CustomDateSelectorWidget(forms.DateInput):
    input_type = 'date'

class AppointmentSerializer(serializers.ModelSerializer):
    day = DateField()
    class Meta:
        model = Appointment
        fields = ['service', 'day', 'time']



class UpdateAppointmentForm(forms.ModelForm):
    def clean(self):
        cleaned_data = super().clean()
        day = cleaned_data.get('day')
        time = cleaned_data.get('time')
        service = cleaned_data.get('service')
        if Appointment.objects.filter(day=day, time=time, service=service).exists():
            raise forms.ValidationError('An appointment already exists for this time and service.')
        return cleaned_data
    

    class Meta:
        model = Appointment
        fields = ['service', 'day', 'time']
        widgets = {
            'day': CustomDateSelectorWidget(),
        }


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']