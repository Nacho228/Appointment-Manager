from rest_framework import serializers
from .models import Appointment

class DateField(serializers.DateField):
    def to_representation(self, value):
        # Convert datetime to date for serialization
        return super().to_representation(value.date()) if value else None

class AppointmentSerializer(serializers.ModelSerializer):
    day = DateField()

    class Meta:
        model = Appointment
        fields = ['service', 'day', 'time']

class UpdateAppointmentForm(AppointmentSerializer):
    pass