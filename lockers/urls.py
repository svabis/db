# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
# ===============================================================
# Skapīšu izvēles skats
    url(r'^/$', 'lockers.views.locker'),


# ===============================================================
# Vēsture
    url(r'^/history/$', 'lockers.views.history'),

# ===============================================================
# check-in
    url(r'^/checkin/(?P<gender>\w+)/(?P<locker_nr>\d+)/$', 'lockers.views.locker_checkin'),
# check-out
    url(r'^/checkout/$', 'lockers.views.locker_checkout'),

# ===============================================================
# Kas klubā
    url(r'^/taken/$', 'lockers.views.persons_in_club'),
# Kas klubā choise
    url(r'^/taken/(?P<c_id>\d+)/$', 'lockers.views.search_by_locker'),

]
