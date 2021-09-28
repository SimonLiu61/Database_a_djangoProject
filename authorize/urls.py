# coding=utf-8
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.showAuth),
    url(r'^login_auth', views.login_site, name='login'),
    url(r'^login_site', views.login_site, name='login'),
    url(r'^logout', views.logout_site, name='logout'),
]