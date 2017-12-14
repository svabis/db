# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
# Abonementu apmaksa
    url(r'^_payment/$', 'subscriptions.views.subscription_payment'),

# Abonementu iesaldēšana
    url(r'^_freeze/$', 'subscriptions.views.subscription_freeze'),


# ===============================================================
# Abonementu izvēles skats
    url(r'^/(?P<back>\w+)/$', 'subscriptions.views.subscription'), # return uz edit, e.t.c.
    url(r'^/$', 'subscriptions.views.subscription'),  # return uz main

]
