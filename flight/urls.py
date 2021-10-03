# coding=utf-8
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^add/$',views.testadd),
    url(r'^bookticket/$', views.bookTicket),
    url(r'^myticket/$', views.myticket),
    url(r'^delticket/$', views.delTicket),
    # url(r'^aircompany/$', views),
    # url(r'^airport/$', views),
    # url(r'^flight/$', views),
    # url(r'^plane/$', views),

    # url(r'^myticket/$', views),
]