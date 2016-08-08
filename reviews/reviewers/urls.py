# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^get_state/(?P<token>\w+)$', views.GetState.as_view(), name='get_state'),
]