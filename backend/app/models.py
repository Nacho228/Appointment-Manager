from django.db import models
from django import forms
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.models import User

SERVICE_CHOICES = (
    ("Doctor care", "Doctor care"),
    ("Nursing care", "Nursing care"),
    ("Medical social services", "Medical social services"),
    ("Basic assistance care", "Basic assistance care"),
    )
TIME_CHOICES = (
    ("3 PM", "3 PM"),
    ("3:30 PM", "3:30 PM"),
    ("4 PM", "4 PM"),
    ("4:30 PM", "4:30 PM"),
    ("5 PM", "5 PM"),
    ("5:30 PM", "5:30 PM"),
    ("6 PM", "6 PM"),
    ("6:30 PM", "6:30 PM"),
    ("7 PM", "7 PM"),
    ("7:30 PM", "7:30 PM"),
)


class Appointment(models.Model):
    class Meta:
        indexes = [
            models.Index(fields=['user']),
            models.Index(fields=['day']),
            models.Index(fields=['time']),
        ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    service = models.CharField(max_length=50, choices=SERVICE_CHOICES, default="Doctor care")
    day = models.DateField(default=timezone.now)
    time = models.CharField(max_length=10, choices=TIME_CHOICES, default="3 PM")
    time_ordered = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self) -> str:
        if self.user:
            return f"{self.user.username} | day: {self.day} | time: {self.time}"
        else:
            return f"No user | day: {self.day} | time: {self.time}" 
 
