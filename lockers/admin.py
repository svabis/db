from django.contrib import admin

from lockers.models import *

# !!!!! Skapji !!!!!
class SkapjiAdmin(admin.ModelAdmin):
    list_display = ['number', 'locker_type', 'checkin_time', 'client']
    list_filter = ['locker_type']


# !!!!! Skapji !!!!!
class Skapji_historyAdmin(admin.ModelAdmin):
    list_display = ['number', 'locker_type', 'checkin_time', 'checkout_time',  'client']
    list_filter = ['locker_type', 'checkin_time', 'checkout_time']


# 'number', 'locker_type', 'checkin_time'

admin.site.register(Skapji, SkapjiAdmin)
admin.site.register(Skapji_history, Skapji_historyAdmin)

