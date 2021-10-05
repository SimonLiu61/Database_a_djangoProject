# coding=utf-8
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^airportmanage', views.airportManagement),
    url(r'^markdelay', views.sendDelayMessage),
    url(r'^canceldelay', views.cancelDelayMessage),
    url(r'^cancelflight', views.cancelFlight),
    url(r'^ticketmanage', views.ticketmanage),

    # url(r'^myticket/$', views),
]