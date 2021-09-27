# coding=utf-8
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    # url(r'^aircompany/$', views),
    # url(r'^airport/$', views),
    # url(r'^flight/$', views),
    # url(r'^plane/$', views),
    # url(r'^bookticket/$', views),
    # url(r'^myticket/$', views),
]