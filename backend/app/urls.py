from django.urls import path
from . import views


urlpatterns = [
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("app/<name>", views.hello_there, name="hello_there"),
    path("", views.home, name="home"),
]
