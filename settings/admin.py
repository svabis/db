from django.contrib import admin

from settings.models import *

# !!!!! Settings !!!!!
class SettingsAdmin(admin.ModelAdmin):
    list_display = ['key', 'value']
    list_filter = ['key']


admin.site.register(Settings, SettingsAdmin)

