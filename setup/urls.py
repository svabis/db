# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
#    url(r'^/checkin/(?P<gender>\w+)/(?P<locker_nr>\d+)/(?P<abon_id>\d+)/$', 'lockers.views.locker_checkin'),


# ===============================================================
# Statusi
    url(r'^status/$', 'setup.views.client_status'),

# ===============================================================
# Apdrošināšanas
    url(r'^insurance/$', 'setup.views.insurance'),

# ===============================================================
# Lietotāji Pievienot
    url(r'^user_add/$', 'setup.views.add_user'),
# Lietotāji Skats
    url(r'^users/$', 'setup.views.system_users'),

# ===============================================================
# Main Setting
    url(r'^$', 'setup.views.settings'),

]
