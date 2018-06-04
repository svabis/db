# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
# ===============================================================
    url(r'^deposit_export/xls/$', 'reports.views.deposit_export'),

# ===============================================================
    url(r'^clients/xls/$', 'reports.views.clients_export'),

# ===============================================================
    url(r'^ab_export/$', 'reports.views.ab_export'),

# ===============================================================
    url(r'^sales_export/$', 'reports.views.sales_export'),

# ===============================================================
    url(r'^lockers_export/xls/$', 'reports.views.lockers_export'),

# ===============================================================
    url(r'^$', 'reports.views.main'),

]
