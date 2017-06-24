from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Appartment, Reservation, Location, Contact

class IndexView(generic.ListView):
    template_name = 'AppartmentRent/index.html'
    context_object_name = 'latest_appartment_list'

    def get_queryset(self):
        return Appartment.objects.order_by('name')

class DetailView(generic.DetailView):
    model = Appartment
    template_name = 'AppartmentRent/detail.html'

    def get_queryset(self):
        return Appartment.objects

class ReservationView(generic.DetailView):
    model = Appartment
    template_name = 'AppartmentRent/reserve.html'

class SuccessView(generic.ListView):
    template_name = 'AppartmentRent/successReservation.html'

class ErrorView(generic.ListView):
    template_name = 'AppartmentRent/errorReservation.html'

class DestinationsView(generic.ListView):
    model = Location
    template_name = 'AppartmentRent/destinations.html'
    context_object_name = 'latest_location_list'

    def get_queryset(self):
        return Location.objects.order_by('place')

class ContactView(generic.TemplateView):
    template_name = 'AppartmentRent/contact.html'

def reserve(request, appartmentId):
    appartment = Appartment.objects.get(id = appartmentId)

    if request.method == 'POST':
        reservation = Reservation()
        reservation.appartment = appartment
        reservation.nameAndSurname = request.POST.get('nameAndSurname')
        reservation.email = request.POST.get('email')
        reservation.personNumber = int(request.POST.get('personNumber'))
        reservation.start_date = request.POST.get('startDate')
        reservation.end_date = request.POST.get('endDate')

        if appartment.checkFreeRooms(1):
            appartment.save(update_fields=['availableRooms'])
            reservation.save()
            return render(request, 'AppartmentRent/successReservation.html', {})
        else :  
            return render(request, 'AppartmentRent/errorReservation.html', {})

def contactUs(request):
    if request.method == 'POST':
        contact = Contact()
        contact.name = request.POST.get('name')
        contact.email = request.POST.get('email')
        contact.title = request.POST.get('title')
        contact.content = request.POST.get('content')  
        contact.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))