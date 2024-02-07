from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("contact", views.contact, name="contact"),
    path("about", views.about, name="about"),
    path("check_authentication/", views.check_authentication, name="check_authentication"),
    path("register/", views.register, name="register"),
    path("booking/", views.booking, name="booking"),
    path("my_appointments/", views.my_appointments, name="my_appointments"),
    path("update_appointment/<int:appointment_id>/", views.update_appointment, name="update_appointment"),
]
