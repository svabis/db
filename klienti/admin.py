from django.contrib import admin

from klienti.models import *


# !!!!! StatusType !!!!!
class StatusTypeAdmin(admin.ModelAdmin):
    list_display = ['status_name', 'status_discount']


# !!!!! Klienti !!!!!
class KlientiAdmin(admin.ModelAdmin):
    list_display = ['surname', 'name', 'client_blocked', 'card_blocked', 'birthday', 'phone', 'e_mail', 'status', 'society', 'status_changed', 'gender', 'reg_date', 's3_nr', 'notes']
    list_filter = ['client_blocked', 'card_blocked', 'status', 'status_changed', 'society', 'gender', 'reg_date']
    search_fields = ['name', 'surname', 'phone', 'e_mail']
#    exclude = []

#'s3_nr', 'client_blocked', 'card_blocked', 'name', 'surname', 'birthday', 'phone', 'e_mail', 'client_blocked', 'status', 'sex', 'reg_date', 'notes'



admin.site.register(Klienti, KlientiAdmin)
admin.site.register(StatusType, StatusTypeAdmin)

