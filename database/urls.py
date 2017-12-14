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

# ===============================================================
# Uzstādījumi
    url(r'^settings/$', 'setup.views.settings'),

# ===============================================================
# Klienti
    url(r'^client/', include('clients.urls')),

# ===============================================================
# Abonementi
    url(r'^subscription', include('subscriptions.urls')),

# ===============================================================
# Skapīši
    url(r'^lockers', include('lockers.urls')),


# ===============================================================
# Clear ID
    url(r'^clear_id/$', 'database.views.clear_id'),

# Main --> Card reader e.t.c.
    url(r'^$', 'database.views.main'),

]
