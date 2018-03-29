# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.contrib import admin

# FOR STATIC AND MEDIA FILE ACCESS
from django.conf import settings

# LOGIN to Django only for authenticated users
from django.contrib.auth.decorators import login_required

admin.autodiscover()
admin.site.login = login_required(admin.site.login)


urlpatterns = [
# STATIC AND MEDIA
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT,}),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT,}),

# LOGINSYS
    url(r'^login/$', 'loginsys.views.login'),
    url(r'^logout/$', 'loginsys.views.logout'),

# Django Admin
    url(r'^admin/', include(admin.site.urls)),

# ===============================================================
# Uzstādījumi
    url(r'^settings/', include('setup.urls')),

# ===============================================================
# Klienti
    url(r'^client/', include('clients.urls')),

# ===============================================================
# Atskaites
    url(r'^reports/', include('reports.urls')),

# ===============================================================
# Abonementi
    url(r'^subscription', include('subscriptions.urls')),

# ===============================================================
# Skapīši
    url(r'^lockers', include('lockers.urls')),


# ===============================================================
# Clear ID
    url(r'^clear_id/$', 'database.views.clear_id'),
# Update Client Notes
    url(r'^update_notes/$', 'database.views.update_notes'),

# Main --> Card reader e.t.c.
    url(r'^', 'database.views.main'),

]
