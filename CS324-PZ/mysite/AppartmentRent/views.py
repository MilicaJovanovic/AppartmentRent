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

# def reserve(request, appartment_id):
#     question = get_object_or_404(Question, pk=question_id)
    # try:
    #     selected_choice = question.choice_set.get(pk=request.POST['choice'])
    # except (KeyError, Choice.DoesNotExist):
    #     # Redisplay the question voting form.
    #     return render(request, 'AppartmentRent/detail.html', {
    #         'question': question,
    #         'error_message': "You didn't select a choice.",
    #     })
    # else:
    #     selected_choice.votes += 1
    #     selected_choice.save()
    #     # Always return an HttpResponseRedirect after successfully dealing
    #     # with POST data. This prevents data from being posted twice if a
    #     # user hits the Back button.
    #     return HttpResponseRedirect(reverse('AppartmentRent:results', args=(question.id,)))