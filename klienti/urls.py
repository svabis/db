# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'main.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

# Jauns Klients
    url(r'^new/$', 'klienti.views.new_client'),

# Rediģēt Klienta kartiņu
    url(r'^edit/(?P<c_id>\d+)/$', 'klienti.views.edit_client'),

# Main --> Redirect UP
    url(r'^$', 'klienti.views.main'),
]
