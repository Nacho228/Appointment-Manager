from rest_framework import serializers
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Appointment

class DateField(serializers.DateField):
    def to_representation(self, value):
        # Convert datetime to date for serialization
        return super().to_representation(value.date()) if value else None

class CustomDateSelectorWidget(forms.DateInput):
    input_type = 'date'

class AppointmentSerializer(serializers.ModelSerializer):
    day = DateField()
    class Meta:
        model = Appointment
        fields = ['service', 'day', 'time']



class UpdateAppointmentForm(forms.ModelForm):
    day = DateField()
    
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