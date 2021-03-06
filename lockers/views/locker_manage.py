# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect

# MultipleObjectsReturned
from django.core.exceptions import MultipleObjectsReturned

from django.core.context_processors import csrf

from database.args import create_args

# Tools
from database.tools import ActiveSubscription, SubscriptionUse

from setup.models import Settings

from clients.models import Klienti
from lockers.models import Skapji, Skapji_history

import unicodedata # locker data unicode normalize

from datetime import datetime

#============================================================
# !!!!! SKAPĪŠU IZVĒLE !!!!!
def locker(request, abon_id):
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

   # Abonementa id
    args['abon_id'] = int(abon_id)

   # LOCKER COLORS FROM SETTINGS
    args['woman_locker_color'] = Settings.objects.get( key = "woman locker color" ).value
    args['man_locker_color'] = Settings.objects.get( key = "man locker color" ).value

    lockers_filled = []

# !!!!!!!!!!!!!!!!
# !!!!! ZERO !!!!!
# !!!!!!!!!!!!!!!!
    lockers_zero = Skapji.objects.filter( locker_type = client.gender, number = 0 ).count()
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
    return render_to_response ( 'locker.html', args )


#============================================================
# !!!! CHECK IN !!!!!
def locker_checkin(request, gender, locker_nr, abon_id):
    args = create_args(request)
    if args['access'] == False:
        return redirect (Settings.objects.get( key = "access denied redirect" ).value)
    if args['loged_in'] == False:
        return redirect("/login/")

    if "active_client" in request.COOKIES:
        c_id = int(request.COOKIES.get(str('active_client')))
        client = Klienti.objects.get( id = c_id )

    try:
       # !!!!! Test if client is not checked in already !!!!!
        locker = Skapji.objects.get( client = client )
    except:
        test = True

        try:
           # !!!!! Test if locker is available !!!!!
            locker = Skapji.objects.get( number = locker_nr, locker_type = str(gender) )
            test = False
            if int( locker_nr ) == 0:
                lockers_zero = Skapji.objects.filter( locker_type = str(gender), number = 0 ).count()
                if lockers_zero < 5:
                    test = True
        except:
            test = True

        if test:
           # !!!!! ABONEMENTA Atkārtots TESTS !!!!!
            check = ActiveSubscription( client )
            if check.exists:
                if check.active.id == int(abon_id):

                    SubscriptionUse( check.active.id )

                    if "search_client" in request.COOKIES:
                        new_checkin = Skapji( number = locker_nr, locker_type = gender, client = client, no_card = True )
                    else:
                        new_checkin = Skapji( number = locker_nr, locker_type = gender, client = client, no_card = False )
                    new_checkin.save()

    return redirect ('/')


#============================================================
# !!!! CHECK OUT !!!!!
def locker_checkout(request):
    args = create_args(request)
    if args['access'] == False:
        return redirect (Settings.objects.get( key = "access denied redirect" ).value)

    if args['loged_in'] == False:
        return redirect("/login/")

    if "active_client" in request.COOKIES:
        c_id = int(request.COOKIES.get(str('active_client')))
        client = Klienti.objects.get( id = c_id )

    try:
        locker = Skapji.objects.get( client = client )
        new_hist = Skapji_history( number = locker.number, locker_type = locker.locker_type, client = locker.client, checkin_time = locker.checkin_time )
        new_hist.save()
        locker.delete()

    except MultipleObjectsReturned:
       # Gļux --> Klients iečekots vairākos skapīšos
        locker = Skapji.objects.filter( client = client )
        new_hist = Skapji_history( number = locker[0].number, locker_type = locker[0].locker_type, client = locker[0].client, checkin_time = locker[0].checkin_time )
        new_hist.save()
        for l in locker:
            l.delete()

    except:
        pass

    return redirect ('/')
