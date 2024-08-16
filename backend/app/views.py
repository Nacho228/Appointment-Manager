from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime, timedelta
from .models import *
from .models import Appointment
from .forms import UpdateAppointmentForm
from .forms import SignUpForm
from django.contrib.auth import login, logout


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse('booking'))
    else:
        form = SignUpForm()
    return render(request, 'registration/register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

def checkTime(times, day, service):
    booked_times = Appointment.objects.filter(day=day, service=service).values_list('time', flat=True)
    available_times = [time for time in times if time not in booked_times]
    return available_times


def home(request):
    success_message = messages.get_messages(request)
    return render(request, 'app/home.html', {'success_message': success_message})

def about(request):
    return render(request, 'app/about.html')

@login_required
def booking(request):
    user = request.user
    weekdays = validWeekday(22)
    validateWeekdays = isWeekdayValid(weekdays)
    services = SERVICE_CHOICES
    times = TIME_CHOICES

    if request.method == 'POST':
        service = request.POST.get('service')
        day = request.POST.get('day')
        time = request.POST.get('time')

        if service is None or day is None or time is None:
            messages.success(request, "Por favor seleccione un servicio, un día y una hora.")
            return redirect('booking')
        
        day = datetime.strptime(day, '%Y-%m-%d')

        today = datetime.now()
        minDate = today
        deltatime = today + timedelta(days=21)
        maxDate = deltatime

        date = dayToWeekday(day)
        hour = checkTime(times, day, service)

        if day <= maxDate and day >= minDate:
            if date in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']:
                if Appointment.objects.filter(day=day).count() < 11:
                    if Appointment.objects.filter(day=day, time=time).count() < 1:
                        appointment = Appointment.objects.create(
                            user=user,
                            service=service,
                            day=day,
                            time=time,
                        )
                        appointment_id = appointment.id
                        messages.success(request, 'Appointment booked successfully')
                        return redirect(reverse('home') + '?success_message=Appointment booked successfully')
                    else:
                        messages.success(request, "The desired time is already taken")
                else:
                    messages.success(request, "The Selected Date Is Incorrect")
            else:
                    messages.success(request, "The Selected Date Isn't In The Correct Time Period!")
        else:
            messages.success(request, "Please Select A Service!")

    return render(request, 'app/booking.html', {
            'weekdays': weekdays,
            'validateWeekdays': validateWeekdays,
            'services': services,
            'times': times,
    })

def my_appointments(request):
    user = request.user
    appointments = Appointment.objects.filter(
        user=user).order_by('day', 'time')

    return render(request, 'app/my_appointments.html', {
        'user': user,
        'appointments': appointments
    })

def update_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, pk=appointment_id, user=request.user)
    if request.method == 'POST':
        if 'update' in request.POST:
            update_form = UpdateAppointmentForm(request.POST, instance=appointment)
            if update_form.is_valid():
                update_form.save()
                return redirect('my_appointments')
        elif 'delete' in request.POST:
            appointment.delete()
        return redirect('my_appointments')
    else:
        form = UpdateAppointmentForm(instance=appointment)

    return render(request, 'app/update_appointment.html', {'form': form, 'appointment': appointment})

def dayToWeekday(x):
    return x.strftime('%A')

def validWeekday(days):
    today = datetime.now()
    weekdays = []
    for i in range(0, days):
        x = today + timedelta(days=i)
        y = x.strftime('%A')
        if y == 'Monday' or y == 'Tuesday' or y == 'Wednesday' or y == 'Thursday' or y == 'Friday':
            weekdays.append(x.strftime('%Y-%m-%d'))
    return weekdays


def isWeekdayValid(x):
    validateWeekdays = []
    for j in x:
        if Appointment.objects.filter(day=j).count() < 10:
            validateWeekdays.append(j)
    return validateWeekdays