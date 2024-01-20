from django.urls import path
from . import views


urlpatterns = [
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("booking/", views.booking, name="booking"),
    path("my_appointments/", views.my_appointments, name="my_appointments"),
    path("update_appointment/<int:appointment_id>/", views.update_appointment, name="update_appointment"),
    path("staffPanel", views.staffPanel, name="staffPanel"),
    path("", views.home, name="home"),
]
