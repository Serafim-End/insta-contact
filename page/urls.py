# coding: utf-8

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^', views.page, name='page'),
    # url(r'^detail', views.follow_detail, name='detail')
]