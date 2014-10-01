from django.shortcuts import render, get_object_or_404
from django.views.generic import UpdateView, ListView
from django.core.urlresolvers import reverse

from web.models import Quorum
from web.forms import QuorumForm


class CheckInView(UpdateView):
    model = Quorum
    template_name = 'checkin.html'
    fields = ['lunch']

    def get_success_url(self):
        return reverse('quorum')


class QuorumView(ListView):
    model = Quorum
    template_name = 'quorum.html'
