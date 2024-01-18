import random
from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime, timedelta
from .models import *
from django.contrib import messages
from .models import Appointment
from .forms import UpdateAppointmentForm
from django.views.generic import ListView


def hello_there(request, name):
    print(request.build_absolute_uri())
    return render(request, 'app/hello_there.html',
                  {
                      'name': name,
                      'date': datetime.now()
                  }
                  )

def home(request):
    return render(request, 'app/home.html')
        
def about(request):
    return render(request, 'app/about.html')

def contact(request):
    return render(request, 'app/contact.html')

def dayToWeekday(x):
    if x is not None:
        z = datetime.strptime(x, "%Y-%m-%d")
        y = z.strftime('%A')
        return y
    else:
        return None

def validWeekday(days):
    #Loop days you want in the next 21 days
    today = datetime.now()
    weekdays = []
    for i in range (0, days):
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

def checkTime(times, day, service):
    #Only show the time of the day and the service that has not been selected before:
    x = []
    for k in times:
        if Appointment.objects.filter(day=day, time=k, service=service).count() < 1:
            x.append(k)
    return x

def checkEditTime(times, day, id):
    #Only show the time of the day that has not been selected before:
    x = []
    appointment = Appointment.objects.get(pk=id)
    time = appointment.time
    for k in times:
        if Appointment.objects.filter(day=day, time=k).count() < 1 or time == k:
            x.append(k)
    return x

def booking(request):
    user = request.user
    weekdays = validWeekday(22)
    validateWeekdays = isWeekdayValid(weekdays)
    services = SERVICE_CHOICES
    times = TIME_CHOICES
    today = datetime.now()
    minDate = today.strftime('%Y-%m-%d')
    deltatime = today + timedelta(days=21)
    strdeltatime = deltatime.strftime('%Y-%m-%d')
    maxDate = strdeltatime

    if request.method == 'POST':
        service = request.POST.get('service')
        day = request.POST.get('day')
        time = request.POST.get('time')
        date = dayToWeekday(day)
        
        if service is None or day is None or time is None:
            messages.success(request, "Por favor seleccione un servicio, un día y una hora.")
            return redirect('booking')
        
        
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
                        messages.success(request, 'Cita guardada con éxito.')
                        return redirect('home')
                    else:
                        messages.success(request, "La hora seleccionada ya está reservada.")
                else:
                    messages.success(request, "El día seleccionado está completo.")
            else:
                messages.success(request, "La fecha seleccionada es incorrecta.")
        else:
            messages.success(request, "La fecha seleccionada no está en el período correcto.")

        request.session['day'] = day
        request.session['service'] = service
        request.session['time'] = time
    
    return render(request, 'app/booking.html', {
            'weekdays': weekdays,
            'validateWeekdays':validateWeekdays,
            'services': services,
            'times': times,
    })


def my_appointments(request):
    user = request.user
    appointments = Appointment.objects.filter(user=user).order_by('day', 'time')
    return render(request, 'app/my_appointments.html', {
        'user': user,
        'appointments': appointments,
    })

def update_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, pk=appointment_id, user=request.user)

    if request.method == 'POST':
        if 'update' in request.POST:
            form = UpdateAppointmentForm(request.POST, instance=appointment)
            if form.is_valid():
                form.save()
        elif 'delete' in request.POST:
            appointment.delete()

        return redirect('my_appointments')
    else:
        form = UpdateAppointmentForm(instance=appointment)
    
    return render(request, 'app/update_appointment.html', {'form': form, 'appointment': appointment})


def staffPanel(request):
    today = datetime.today()
    minDate = today.strftime('%Y-%m-%d')
    deltatime = today + timedelta(days=21)
    strdeltatime = deltatime.strftime('%Y-%m-%d')
    maxDate = strdeltatime
    #Only show the Appointments 21 days from today
    items = Appointment.objects.filter(day__range=[minDate, maxDate]).order_by('day', 'time')

    return render(request, 'app/staffPanel.html', {
        'items':items,
    })

