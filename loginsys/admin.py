from django.contrib import admin
from loginsys.models import *


class LoginAdmin(admin.ModelAdmin):
    list_display = ['date', 'event', 'user']
    list_filter = ['date', 'event', 'user']


class LogAdmin(admin.ModelAdmin):
    list_display = ['log_user', 'log_date', 'log_event', 'log_event_data']
    list_filter = ['log_user', 'log_date', 'log_event']
#    search_fields = ['vards', 'e_pasts', 'tel']
#    exclude = ['pirmais_pieteikums', 'pedejais_pieteikums', 'atteikuma_reizes', 'pieteikuma_reizes']

admin.site.register(Log, LogAdmin)
admin.site.register(Login, LoginAdmin)

