# -*- coding: utf-8 -*-
from django.contrib import admin
from subscriptions.models import *


# !!!!! Abonementu_tipi !!!!!
class AbonementTypeAdmin(admin.ModelAdmin):
    list_display = ['title', 'created', 'available', 'position', 'price', 'special', 'first_time', 'best_before', 'time_limit', 'time_limit_type', 'times', 'times_count', 's3_nr']
    list_filter = ['created', 'position', 'available', 'special', 'first_time', 'best_before', 'time_limit', 'times', 'times_count']
#    search_fields = []
#    exclude = []


# !!!!! Abonementi !!!!!
class AbonementiAdmin(admin.ModelAdmin):
    list_display = ['purchase_date', 'client', 'subscr', 'price', 'active', 'ended', 'frozen', 'frozen_until_date', 'activation_date', 'activate_before', 'best_before', 'times_count']
    list_filter = ['purchase_date', 'active', 'ended', 'frozen', 'frozen_until_date', 'activation_date', 'activate_before', 'best_before', 'times_count', 'subscr']
#    search_fields = ['client']
#    exclude = []


# !!!!! Laika Limiti !!!!!
class TimelimitTypeAdmin(admin.ModelAdmin):
    list_display = ['title', 'weekday1', 'weekday1_start_time', 'weekday1_end_time', 'weekday2', 'weekday2_start_time', 'weekday2_end_time', 'weekend', 'weekend_start_time', 'weekend_end_time']
    list_filter = ['title', 'weekday1', 'weekday2', 'weekend']


admin.site.register(AbonementType, AbonementTypeAdmin)
admin.site.register(Abonementi, AbonementiAdmin)
admin.site.register(TimelimitType, TimelimitTypeAdmin)
