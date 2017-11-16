# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.contrib import admin

# FOR STATIC AND MEDIA FILE ACCESS
from django.conf import settings

# LOGIN to Django only for authenticated users
from django.contrib.auth.decorators import login_required
admin.site.login = login_required(admin.site.login)

#admin.autodiscover()

urlpatterns = [

# STATIC AND MEDIA
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT,}),
#    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT,}),

# Django Admin
    url(r'^admin/', include(admin.site.urls)),

# NEW CLIENT
    url(r'^new_client$', 'klienti.views.new_client'),

# Main --> Shodienas nodarbibas
    url(r'^$', 'database.views.main'),

]
