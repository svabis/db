# -*- coding: utf-8 -*-
from django.contrib import admin
from subscriptions.models import *

# Register your models here.

# !!!!! Abonementu_tipi !!!!!
class AbonementTypeAdmin(admin.ModelAdmin):
    list_display = ['title', 'short_title', 'position', 'price', 'special', 'first_time', 'best_before', 'time_limit', 'time_limit_type', 'times', 'times_count']
    list_filter = ['title', 'short_title', 'position', 'price', 'special', 'first_time', 'best_before', 'time_limit', 'time_limit_type', 'times', 'times_count']
#    search_fields = []
#    exclude = []

# 'title', 'price', 'active', 'first_time', 'best_before', 'time_limit', 'times', 'times_count'



# !!!!! Abonementi !!!!!
class AbonementiAdmin(admin.ModelAdmin):
    list_display = ['title', 'client', 'price', 'purchase_date', 'active', 'first_time', 'best_before', 'times', 'times_count']
    list_filter = ['title', 'price', 'purchase_date', 'active', 'first_time', 'best_before', 'times', 'times_count']

    search_fields = ['client']
#    exclude = []

# 'title', 'client', 'price', 'purchase_date', 'active', 'first_time', 'best_before', 'times', 'times_count'
# 'time_limit'


# !!!!! Laika Limiti !!!!!
class TimelimitTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'weekday', 'start_time', 'end_time']
    list_filter = ['name', 'weekday', 'start_time', 'end_time']


admin.site.register(AbonementType, AbonementTypeAdmin)
admin.site.register(Abonementi, AbonementiAdmin)
admin.site.register(TimelimitType, TimelimitTypeAdmin)
