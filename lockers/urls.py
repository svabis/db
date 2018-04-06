# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
# ===============================================================
# Skapīšu izvēles skats
    url(r'^/(?P<abon_id>\d+)/$', 'lockers.views.locker'),

# Skapīšu maiņas skats
    url(r'^/change/$', 'lockers.views.locker_change'),
    url(r'^/changer/(?P<gender>\w+)/(?P<locker_nr>\d+)/$', 'lockers.views.locker_changer'),

# ===============================================================
# Eksports
    url(r'^/history/csv/$', 'lockers.views.history_csv'),
    url(r'^/history/xls/$', 'lockers.views.history_xls'),

# ===============================================================
# Vēsture
    url(r'^/history/(?P<pageid>\d+)/$', 'lockers.views.history'),
    url(r'^/history/$', 'lockers.views.history'),

# ===============================================================
# check-in
    url(r'^/checkin/(?P<gender>\w+)/(?P<locker_nr>\d+)/(?P<abon_id>\d+)/$', 'lockers.views.locker_checkin'),
# check-out
    url(r'^/checkout/$', 'lockers.views.locker_checkout'),

# ===============================================================
# Kas klubā
    url(r'^/taken/$', 'lockers.views.persons_in_club'),
# Kas klubā
    url(r'^/taken/count/$', 'lockers.views.in_club_count'),
# Kas klubā choise
    url(r'^/taken/(?P<c_id>\d+)/$', 'lockers.views.search_by_locker'),

]
