# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
# ===============================================================
# AB cancel (Admin only)
    url(r'^/cancel/(?P<ab_id>\d+)/(?P<back>\d+)/(?P<pageid>\d+)/$', 'subscriptions.views.ab_cancel'),
    url(r'^/cancel/(?P<ab_id>\d+)/(?P<back>\d+)/$', 'subscriptions.views.ab_cancel'),

# ===============================================================
# History export
    url(r'^/history/xls/$', 'subscriptions.views.subscription_history_xls'),

# History
    url(r'^/history/(?P<pageid>\d+)/(?P<back>\d+)/$', 'subscriptions.views.subscription_history', name='subscr_hist'),
    url(r'^/history/(?P<back>\d+)/$', 'subscriptions.views.subscription_history', name='subscr_hist'),

# ===============================================================
# Abonementu apmaksa
    url(r'^_payment/$', 'subscriptions.views.subscription_payment'),

# Abonementu pirkums
    url(r'^_purchase/$', 'subscriptions.views.subscription_purchase'),

# ===============================================================
# Abonementu iesaldēšana
    url(r'^_freeze/$', 'subscriptions.views.subscription_freeze'),
# Iesaldes atcelšana
    url(r'^_unfreeze/$', 'subscriptions.views.subscription_unfreeze'),

# ===============================================================
# Abonementu izvēles skats
    url(r'^/(?P<back>\w+)/$', 'subscriptions.views.subscription'), # return uz edit, e.t.c.
    url(r'^/$', 'subscriptions.views.subscription'),  # return uz main

]
