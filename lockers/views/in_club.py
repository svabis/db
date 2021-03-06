# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect

# JSON
from django.http import JsonResponse

from database.args import create_args

from setup.models import Settings

from clients.models import Klienti
from lockers.models import Skapji, Skapji_history

# import paginator
#from database.paginator import Paginator
#import math


#============================================================
# !!!!! Kas Klubā !!!!!
def persons_in_club(request):
    args = create_args(request)
    if args['access'] == False:
        return redirect (Settings.objects.get( key = "access denied redirect" ).value)

   # LOCKER COLORS FROM SETTINGS
    args['woman_locker_color'] = Settings.objects.get( key = "woman locker color" ).value
    args['man_locker_color'] = Settings.objects.get( key = "man locker color" ).value

    args['active_tab_4'] = True

    args['data_no_card'] = Skapji.objects.filter( no_card = True ).order_by( 'checkin_time' )
    args['data'] = Skapji.objects.filter( no_card = False ).order_by( 'checkin_time' )

    return render_to_response ( 'in_club.html', args )


#============================================================
# !!!!! Kas Klubā (SKAITS)!!!!!
def in_club_count(request):
    args = create_args(request)
    if args['access'] == False:
        return redirect (Settings.objects.get( key = "access denied redirect" ).value)

    data = {}
    data['count'] = Skapji.objects.all().count()
    if args['loged_in'] == True:
        return JsonResponse(data)

    data['count'] = 0
    return JsonResponse(data)


#============================================================
# !!!!! Klientu Meklēšanas pēc skapīša !!!!!
def search_by_locker(request, c_id):
    args = create_args(request)
    if args['access'] == False:
        return redirect (Settings.objects.get( key = "access denied redirect" ).value)

    if args['loged_in'] == False:
        return redirect("/login/")

    client = Klienti.objects.get( id = c_id )

    response = redirect ("/")
    response.set_cookie( key='active_client', value=client.id )
    return response
