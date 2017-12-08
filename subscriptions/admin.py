# -*- coding: utf-8 -*-
from django.contrib import admin
from subscriptions.models import *

# Register your models here.

# !!!!! Abonementu_tipi !!!!!
class AbonementTypeAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'special', 'first_time', 'best_before', 'time_limit', 'times', 'times_count']
    list_filter = ['title', 'price', 'special', 'first_time', 'best_before', 'time_limit', 'times', 'times_count']
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

admin.site.register(AbonementType, AbonementTypeAdmin)
admin.site.register(Abonementi, AbonementiAdmin)


