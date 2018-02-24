# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect

#from django.core.context_processors import csrf

#from django.db.models import Q # search in multiple columns

#from clients.forms import KlientsForm
from clients.models import Klienti, Blacklist

#from setup.models import Settings

#from database.args import create_args

#from clients.paginator import Paginator  # import paginator
#import math # for rounding up Page Counter


#==================================================================
# !!!!! Blacklist Add !!!!!
def add_to_blacklist(request):
   # Get Active client from COOKIE
    if "active_client" in request.COOKIES:
        try:
            c_id = int(request.COOKIES.get(str('active_client')))
            client = Klienti.objects.get( id = c_id )
            if request.POST:
                reason = request.POST.get('blacklist_reason', '')

                new_bl = Blacklist( bl_user = client, bl_data = reason )
                new_bl.save()

                client.client_blocked = True
                client.save()
        except:
            pass
    return redirect("/client/edit/")


#==================================================================
#!!!!!! Blacklist remove !!!!!
def remove_from_blacklist(request):
   # Get Active client from COOKIE
    if "active_client" in request.COOKIES:
        try:
            c_id = int(request.COOKIES.get(str('active_client')))
            client = Klienti.objects.get( id = c_id )
            if request.POST:
                client.client_blocked = False
                client.save()
        except:
            pass
    return redirect("/client/edit/")
