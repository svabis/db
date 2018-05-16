from django.contrib import admin
from loginsys.models import *


class LoginAdmin(admin.ModelAdmin):
    list_display = ['date', 'ip', 'event', 'user']
    list_filter = ['date', 'ip', 'event', 'user']


class ReportsAdmin(admin.ModelAdmin):
    list_display = ['date', 'event', 'event_data', 'user']
    list_filter = ['date', 'event', 'user']


admin.site.register(Login, LoginAdmin)
admin.site.register(Reports, ReportsAdmin)

