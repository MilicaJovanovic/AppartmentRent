from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Appartment, Reservation

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

class SuccessReservationView(generic.DetailView):
    model = Appartment
    template_name = 'AppartmentRent/successReservation.html'

class ErrorReservationView(generic.DetailView):
    model = Appartment
    template_name = 'AppartmentRent/errorReservation.html'
