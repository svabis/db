# -*- coding: utf-8 -*-
from django.contrib import admin

from clients.models import *

# !!!!! Blacklist !!!!!
class BlacklistAdmin(admin.ModelAdmin):
    list_display = ['bl_user', 'bl_date', 'bl_data']
    list_filter = ['bl_date']
    search_fields = ['bl_user']

# !!!!! Statusi !!!!!
class StatusiAdmin(admin.ModelAdmin):
    list_display = ['status_name', 'status_discount']


# !!!!! Klienti !!!!!
class KlientiAdmin(admin.ModelAdmin):
    list_display = ['surname', 'name', 'card_nr', 'client_blocked', 'card_blocked', 'birthday', 'phone', 'e_mail', 'status', 'society', 'status_changed', 'gender', 'reg_date', 's3_nr', 'notes']
    list_filter = ['client_blocked', 'card_blocked', 'status', 'status_changed', 'society', 'gender', 'reg_date']
    search_fields = ['name', 'surname', 'phone', 'e_mail', 'card_nr']


# !!!!! Iesalde !!!!!
class IesaldeAdmin(admin.ModelAdmin):
    list_display = ['i_client', 'i_date', 'i_amount']
    list_filter = ['i_date']


# !!!!! Depozīts !!!!!
class DepositAdmin(admin.ModelAdmin):
    list_display = ['d_client', 'd_date', 'd_amount']
    list_filter = ['d_date']



admin.site.register(Klienti, KlientiAdmin)
admin.site.register(Statusi, StatusiAdmin)

admin.site.register(Iesalde, IesaldeAdmin)
admin.site.register(Deposit, DepositAdmin)

admin.site.register(Blacklist, BlacklistAdmin)
