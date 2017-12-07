from django.contrib import admin
from subscriptions.models import *

# Register your models here.

# !!!!! Abonementi !!!!!
class AbonementiAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'special', 'first_time', 'best_before', 'time_limit', 'times', 'times_count']
    list_filter = ['title', 'price', 'special', 'first_time', 'best_before', 'time_limit', 'times', 'times_count']
#    search_fields = ['name', 'surname', 'phone', 'e_mail']
#    exclude = []

# 'title', 'price', 'active', 'first_time', 'best_before', 'time_limit', 'times', 'times_count'


admin.site.register(Abonementi, AbonementiAdmin)


