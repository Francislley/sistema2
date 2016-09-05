#!/usr/bin/env python3
#antuor:Alan

from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.publish, name='publish'),
    url(r'^$',views.borrow,name='borrow'),
]