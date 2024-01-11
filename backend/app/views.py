from django.shortcuts import render, redirect
from datetime import datetime, timedelta
from .models import *
from django.contrib import messages
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
    z = datetime.strptime(x, "%Y-%m-%d")
    y = z.strftime('%A')
    return y

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

def checkTime(times, day):
    #Only show the time of the day that has not been selected before:
    x = []
    for k in times:
        if Appointment.objects.filter(day=day, time=k).count() < 1:
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
    weekdays = validWeekday(22)
    validateWeekdays = isWeekdayValid(weekdays)

    if request.method == 'POST':
        service = request.POST.get('service')
        day = request.POST.get('day')
        if service == None:
            messages.success(request, "Porfavor seleccione un servicio")
            return redirect('booking')

        request.session['day'] = day
        request.session['service'] = service

        return redirect('bookingSumbit')
    
    return render(request, 'booking.html', {
            'weekdays':weekdays,
            'validateWeekdays':validateWeekdays,
    })

