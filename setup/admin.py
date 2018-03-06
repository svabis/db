# -*- coding: utf-8 -*-
from django.contrib import admin

from setup.models import *

# !!!!! Settings !!!!!
class SettingsAdmin(admin.ModelAdmin):
    list_display = ['key', 'value']
    list_filter = ['key']

# !!!!! Apdrošinātāji !!!!!
class ApdrosinatajiAdmin(admin.ModelAdmin):
    list_display = ['title', 'visible']
    list_filter = ['visible']


admin.site.register(Settings, SettingsAdmin)
admin.site.register(Apdrosinataji, ApdrosinatajiAdmin)
