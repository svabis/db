from django.contrib import admin

from klienti.models import *

# !!!!! Klienti !!!!!
class KlientiAdmin(admin.ModelAdmin):
    list_display = ['surname', 'name', 'client_blocked', 'card_blocked', 'birthday', 'phone', 'e_mail', 'status', 'status_changed', 'society',  'gender', 'reg_date', 'notes']
    list_filter = ['client_blocked', 'card_blocked', 'status', 'status_changed', 'society', 'gender', 'reg_date']
    search_fields = ['name', 'surname', 'phone', 'e_mail']
#    exclude = []

#'client_blocked', 'card_blocked', 'name', 'surname', 'birthday', 'phone', 'e_mail', 'client_blocked', 'status', 'sex', 'reg_date', 'notes'

admin.site.register(Klienti, KlientiAdmin)

