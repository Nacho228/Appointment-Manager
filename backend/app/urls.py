from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('accounts/register/', views.register, name='register'),
    path('accounts/logout/', views.logout_view, name='logout'),
    path("", views.home, name="home"),
    path("about", views.about, name="about"),
    path("booking/", views.booking, name="booking"),
    path("my_appointments/", views.my_appointments, name="my_appointments"),
    path("update_appointment/<int:appointment_id>/", views.update_appointment, name="update_appointment"),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)