# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.contrib import admin

# FOR STATIC AND MEDIA FILE ACCESS
from django.conf import settings

# !!!!! DISABLED UNTIL USER LOGIN CREATED !!!!!
# LOGIN to Django only for authenticated users
#from django.contrib.auth.decorators import login_required

#admin.site.login = login_required(admin.site.login)
# !!!!! DISABLED UNTIL USER LOGIN CREATED !!!!!

urlpatterns = [
# STATIC AND MEDIA
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT,}),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT,}),

# Django Admin
    url(r'^admin/', include(admin.site.urls)),


# Klienti
    url(r'^client/', include('klienti.urls')),


# Skapīši
    url(r'^locker/$', 'database.views.locker'),

# Abonementi
    url(r'^subscription/$', 'database.views.subscription'),


# Clear ID
    url(r'^clear_id/$', 'database.views.clear_id'),


# Search Klient
    url(r'^search/$', 'database.views.search'),
# Search rezultāts
    url(r'^search_response/(?P<c_id>\d+)/$', 'database.views.search_response'),


# Main --> Shodienas nodarbibas
    url(r'^$', 'database.views.main'),

]
