# coding=utf-8
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^manage', views.companyManage),
    url(r'^ticketmanage', views.ticketmanage),

    # url(r'^myticket/$', views),
]