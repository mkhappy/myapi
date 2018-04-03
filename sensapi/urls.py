# -*- coding: utf-8 -*-

from django.conf.urls import url
from sensapi import views

urlpatterns = [
    url(r'^$', views.SensView.as_view()),
    #url(r'^(?P<pk>[0-9]+)/$', views.SensView.as_view()),
]
