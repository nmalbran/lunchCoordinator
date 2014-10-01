from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import UpdateView, ListView, View
from django.core.urlresolvers import reverse

from web.models import Quorum, Place
from web.forms import QuorumForm


class CheckInView(UpdateView):
    model = Quorum
    template_name = 'checkin.html'
    fields = ['lunch']

    def get_success_url(self):
        return reverse('quorum')

class RSVP(View):
    def get(self, request, pk, rsvp):
        q = get_object_or_404(Quorum, pk=pk)
        y = {1:'yes', 0:'no'}
        q.lunch = y[int(rsvp)]
        q.save()
        return redirect('quorum')


class QuorumView(ListView):
    model = Quorum
    template_name = 'quorum.html'

    def get_context_data(self, **kwargs):
        context = super(QuorumView, self).get_context_data(**kwargs)
        context['places'] = Place.objects.all()
        return context

class PlacesView(ListView):
    model = Place
    template_name = 'places.html'
