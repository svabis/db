# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect

from django.core.context_processors import csrf

from database.args import create_args

from setup.models import Settings

from clients.models import Klienti
from lockers.models import Skapji

import unicodedata # locker data unicode normalize

from datetime import datetime

#============================================================
# !!!!! SKAPĪŠU MAIŅAS IZVĒLE !!!!!
def locker_change(request):
    args = create_args(request)
    if args['access'] == False:
        return redirect (Settings.objects.get( key = "access denied redirect" ).value)

    if args['loged_in'] == False:
        return redirect("/login/")

    if "active_client" in request.COOKIES:
        c_id = int(request.COOKIES.get(str('active_client')))
        client = Klienti.objects.get( id = c_id )
    else:
        redirect ("/")

   # DISABLED LOCKERS
    dml_value = Settings.objects.get( key = "disabled man locker" ).value
    dwl_value = Settings.objects.get( key = "disabled woman locker" ).value
   # convert unicode to string
    dml_value = unicodedata.normalize('NFKD', dml_value).encode('ascii','ignore')
    dwl_value = unicodedata.normalize('NFKD', dwl_value).encode('ascii','ignore')

   # split string to array
    dml = dml_value.split(",")
    dwl = dwl_value.split(",")

   # convert arrays to int
    dml = map(int, dml)
    dwl = map(int, dwl)

    args['dm'] = dml
    args['dw'] = dwl

   # LOCKER COLORS FROM SETTINGS
    args['woman_locker_color'] = Settings.objects.get( key = "woman locker color" ).value
    args['man_locker_color'] = Settings.objects.get( key = "man locker color" ).value

    lockers_filled = []
# !!!!!!!!!!!!!!!!
# !!!!! ZERO !!!!!
# !!!!!!!!!!!!!!!!
    lockers_zero = Skapji.objects.filter( locker_type = client.gender, number = 0 ).count()
    args['zero'] = lockers_zero
    if lockers_zero > 4:
        lockers_filled.append( 0 )
# ----------------

   # get locker numbers in use
    lockers_temp = Skapji.objects.filter( locker_type = client.gender ).exclude( number = 0 )
    for n in lockers_temp:
        lockers_filled.append( int(n.number) )

   # ADD DISABLED LOCKERS
    if client.gender == "V":
        lockers_filled = lockers_filled + dml
    else:
        lockers_filled = lockers_filled + dwl

    lockers = []
   # MALE LOCKERS
    if client.gender == "V":
       for i in range(0, int(Settings.objects.get( key = "man locker count" ).value) + 1 ):
           if i not in lockers_filled:
               lockers.append([i,0])
           else:
               lockers.append([i,1])

   # FEMALE LOCKERS
    else:
       for i in range(0, int(Settings.objects.get( key = "woman locker count" ).value) + 1 ):
           if i not in lockers_filled:
               lockers.append([i,0])
           else:
               lockers.append([i,1])

    args['lockers'] = lockers
    args['gender'] = client.gender
    return render_to_response ( 'locker_change.html', args )


#============================================================
# !!!! SKAPĪŠA MAIŅA !!!!!
def locker_changer(request, gender, locker_nr):
    args = create_args(request)
    if args['access'] == False:
        return redirect (Settings.objects.get( key = "access denied redirect" ).value)

    if args['loged_in'] == False:
        return redirect("/login/")

    if "active_client" in request.COOKIES:
        c_id = int(request.COOKIES.get(str('active_client')))
        client = Klienti.objects.get( id = c_id )

    try:
       # !!!!! GET Skapji object client is checked in already !!!!!
        locker = Skapji.objects.get( client = client )
        locker.number = locker_nr
        locker.save()
    except:
        pass

    return redirect ('/')
