from django.urls import path
from . import views


urlpatterns = [
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("booking/", views.booking, name="booking"),
    path('bookingSubmit', views.bookingSubmit, name='bookingSubmit'),
    path("userPanel/", views.userPanel, name="userPanel"),
    path("userUpdate/", views.userUpdate, name="userUpdate"),
    path("staffPanel", views.staffPanel, name="staffPanel"),
    path("app/<name>", views.hello_there, name="hello_there"),
    path("", views.home, name="home"),
]
