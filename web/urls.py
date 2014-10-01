from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView

from web.views import CheckInView, QuorumView, RSVP, PlacesView

UUID = r'[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}'

urlpatterns = patterns('',

    url(r'^/?$', RedirectView.as_view(url='quorum/')),

    #url(r'^checkin/(?P<pk>' + UUID + ')/?$', CheckInView.as_view(), name='checkin'),
    url(r'^rsvp/(?P<pk>' + UUID + ')(?P<rsvp>[10]{1})/?$', RSVP.as_view(), name='rsvp'),
    url(r'^quorum/?$', QuorumView.as_view(), name='quorum'),
    # url(r'^places/?$', PlacesView.as_view(), name='places'),

)
