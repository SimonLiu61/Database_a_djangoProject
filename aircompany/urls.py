# coding=utf-8
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^manage', views.companyManage),

    # url(r'^myticket/$', views),
]