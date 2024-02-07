import random
from rest_framework.response import Response
from django.http import JsonResponse
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth import authenticate, login  
from rest_framework.renderers import JSONRenderer
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime, timedelta
from .models import *
from .models import Appointment
from .forms import UpdateAppointmentForm

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def check_authentication(request):
    return Response({'authenticated': True, 'username': request.user.username})

@csrf_exempt
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return JsonResponse({'message': 'Successful register and log in', 'success': True})
            else:
                return JsonResponse({'message': 'Unable to authenticate the user', 'success': False})
        else:
            errors = dict(form.errors.items())
            return JsonResponse({'errors': errors, 'success': False})
    else:
        return JsonResponse({'message': 'Invalid request method', 'success': False})

def home(request):
    return render(request, 'app/home.html')

def about(request):
    return render(request, 'app/about.html')

def contact(request):
    return render(request, 'app/contact.html')

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def booking(request):

    weekdays = validWeekday(22)
    validate_weekdays = isWeekdayValid(weekdays)
    today = datetime.now()
    min_date = today.strftime('%Y-%m-%d')
    delta_time = today + timedelta(days=21)
    max_date = delta_time.strftime('%Y-%m-%d')

    if request.method == 'GET':
        response_data = {
            'services': [service[0] for service in SERVICE_CHOICES],
            'days': [day for day in validWeekday(22)],
            'times': [time[0] for time in TIME_CHOICES],
        }
        return JsonResponse(response_data)

    
    if request.method == 'POST':
        service = request.data.get('service')
        day = request.data.get('day')
        time = request.data.get('time')
    
        if service is None or day is None or time is None:
            return JsonResponse({'message': 'Por favor, seleccione un servicio, una fecha y una hora.'})

        try:
            day = datetime.strptime(day, '%Y-%m-%d')
            max_date = datetime.strptime(max_date, '%Y-%m-%d')
            min_date = datetime.strptime(min_date, '%Y-%m-%d')
        except ValueError:
            return JsonResponse({'message': "La fecha seleccionada es incorrecta."})
    

        date = dayToWeekday(day)

        if day <= max_date and day >= min_date:
                print("Date is within the valid range.")
                if date in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']:
                    print("Day is a valid weekday.")
                    if Appointment.objects.filter(day=day).count() < 11:
                        if Appointment.objects.filter(day=day, time=time).count() < 1:
                            user = request.user
                            appointment = Appointment.objects.create(
                                user=user,
                                service=service,
                                day=day,
                                time=time,
                            )
                            serializer = UpdateAppointmentForm(appointment)
                            serialized_data = serializer.data
                            return JsonResponse({'message': 'Cita guardada con éxito.', 'success': True})
                        else:
                            return JsonResponse({'message': "La hora seleccionada ya está reservada.", 'success': False})
                    else:
                        return JsonResponse({'message': "El día seleccionado está completo."})
                else:
                    return JsonResponse({'message': "La fecha seleccionada es incorrecta."})
        
        json_data = JSONRenderer().render(serialized_data)
        return json_data

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def my_appointments(request):
    user = request.user
    appointments = Appointment.objects.filter(
        user=user).order_by('day', 'time')

    appointments_data = []
    for appointment in appointments:
        appointments_data.append({
            'id': appointment.id,
            'service': appointment.service,
            'day': appointment.day.strftime('%Y-%m-%d'),
            'time': appointment.time,
        })

    response_data = {'user': user.username, 'appointments': appointments_data}
    return JsonResponse(response_data)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def update_appointment(request, appointment_id):
    appointment = get_object_or_404(
        Appointment, pk=appointment_id, user=request.user)

    if request.method == 'GET':
        # Return details of the appointment
        appointment_data = {
            'id': appointment.id,
            'service': appointment.service,
            'day': appointment.day.strftime('%Y-%m-%d'),
            'time': appointment.time,
        }
        return JsonResponse(appointment_data)

    elif request.method == 'PUT':
        # Update the appointment
        form = UpdateAppointmentForm(request.data, instance=appointment)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True, 'message': 'Appointment updated successfully'})
        else:
            return JsonResponse({'success': False, 'errors': form.errors}, status=400)

    elif request.method == 'DELETE':
        # Delete the appointment
        appointment.delete()
        return JsonResponse({'success': True, 'message': 'Appointment deleted successfully'})

    return JsonResponse({'success': False, 'message': 'Invalid request method'}, status=400)


def dayToWeekday(x):
    return x.strftime('%A')

def validWeekday(days):
    # Loop days you want in the next 21 days
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