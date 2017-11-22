# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
# Search rezultāts
    url(r'^search_response/(?P<c_id>\d+)/$', 'klienti.views.search_response'),
# Search Klient
    url(r'^search/(?P<pageid>\d+)/$', 'klienti.views.search'), # COOKIE page = pageid
    url(r'^search/$', 'klienti.views.search'), # POST --> page=1

#==============================================================================

# Jauns Klients
    url(r'^new/$', 'klienti.views.new_client'),

# Rediģēt Klienta kartiņu
    url(r'^edit/$', 'klienti.views.edit_client'),


# Main --> Redirect UP
    url(r'^$', 'klienti.views.main'),
]
