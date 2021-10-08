# coding=utf-8
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^manage', views.companyManage),
    url(r'^ticketmanage', views.ticketmanage),
    url(r'^addflight', views.addflight),
    url(r'^planemanage', views.planeManage),
    url(r'^planeedit', views.planesEdit),
    url(r'^addplane', views.addPlane),

    # url(r'^myticket/$', views),
]