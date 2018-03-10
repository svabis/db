# -*- coding: utf-8 -*-
from django.contrib import admin

from clients.models import *

# !!!!! Blacklist !!!!!
class BlacklistAdmin(admin.ModelAdmin):
    list_display = ['bl_user', 'bl_client', 'bl_date', 'bl_data']
    list_filter = ['bl_date']
    search_fields = ['bl_client']

# !!!!! Statusi !!!!!
class StatusiAdmin(admin.ModelAdmin):
    list_display = ['status_name', 'status_discount']


# !!!!! Klienti !!!!!
class KlientiAdmin(admin.ModelAdmin):
    list_display = ['surname', 'name', 'card_nr', 'client_blocked', 'card_blocked', 'birthday', 'phone', 'e_mail', 'status', 'society', 'status_changed', 'gender', 'reg_date',
       'disabled', 'disabled_until', 'student', 'student_until', 'elderly', 's3_nr', 'notes', 'frozen', 'frozen_from', 'frozen_until']
    list_filter = ['client_blocked', 'card_blocked', 'frozen', 'status', 'status_changed', 'society', 'gender', 'reg_date']
    search_fields = ['name', 'surname', 'phone', 'e_mail', 'card_nr', 's3_nr']



# !!!!! Depozīts !!!!!
class DepositAdmin(admin.ModelAdmin):
    list_display = ['d_date', 'd_user', 'd_client', 'd_reason', 'd_added', 'd_remain']
    list_filter = ['d_user', 'd_date']



admin.site.register(Klienti, KlientiAdmin)
admin.site.register(Statusi, StatusiAdmin)

admin.site.register(Deposit, DepositAdmin)

admin.site.register(Blacklist, BlacklistAdmin)
