from django.contrib import admin

from lockers.models import *

# !!!!! Skapji !!!!!
class SkapjiAdmin(admin.ModelAdmin):
    list_display = ['number', 'locker_type', 'checkin_time', 'client']
    list_filter = ['locker_type']


# 'number', 'locker_type', 'checkin_time'

admin.site.register(Skapji, SkapjiAdmin)

