from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'lunchCoordinator.views.home', name='home'),

    url(r'^', include('web.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
