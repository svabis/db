# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
# ===============================================================
    url(r'^sales_export/$', 'reports.views.sales_export'),

# ===============================================================
    url(r'^clients/xls/$', 'reports.views.clients_export'),

# ===============================================================
    url(r'^bs/xls/$', 'reports.views.bs_export'),

# ===============================================================
    url(r'^$', 'reports.views.main'),

]
