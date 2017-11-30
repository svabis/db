# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect

from django.core.context_processors import csrf

from database.args import create_args

from setup.models import Settings

from klienti.models import Klienti
from lockers.models import Skapji

#============================================================
# !!!!! SKAPĪŠI !!!!!
def locker(request):
    args = create_args(request)
    if args['access'] == False:
        return redirect (Settings.objects.get( key = "access denied redirect" ).value)

    if "active_client" in request.COOKIES:
        c_id = int(request.COOKIES.get(str('active_client')))
        client = Klienti.objects.get( id = c_id )
    else:
        redirect ("/")

    lockers_filled = []
#    lockers_filled = Skapji.objects.filter( locker_type = client.gender ) #.values( 'number' )
    lockers_temp = Skapji.objects.filter( locker_type = client.gender ) #.values( 'number' )

    for n in lockers_temp:
        lockers_filled.append( int(n.number) )

    lockers = []

   # MALE LOCKERS
    if client.gender == "V":
       for i in range(1,106):
           if i not in lockers_filled:
               lockers.append([i,0])
           else:
               lockers.append([i,1])

   # FEMALE LOCKERS
    else:
       for i in range(1,177):
           if i not in lockers_filled:
               lockers.append([i,0])
           else:
               lockers.append([i,1])

    args['lockers'] = lockers
    args['gender'] = client.gender

    return render_to_response ( 'locker.html', args )


# !!!! CHECK IN !!!!!
def locker_checkin(request, gender, locker_nr):
    if "active_client" in request.COOKIES:
        c_id = int(request.COOKIES.get(str('active_client')))
        client = Klienti.objects.get( id = c_id )

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# !!!!! Test if locker is available !!!!!
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# !!!!! Test if client is not checked in already !!!!!
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    new_checkin = Skapji( number = locker_nr, locker_type = gender, client = client )
    new_checkin.save()

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# !!!!! respone ar COOKIE - iečekots, OR SOMTHING LIKE THAT !!!!!
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    return redirect ('/')


#============================================================
# !!!!! Kas Klubā !!!!!
def persons_in_club(request):
    args = create_args(request)
    if args['access'] == False:
        return redirect (Settings.objects.get( key = "access denied redirect" ).value)

    args['data'] = Skapji.objects.all().order_by( 'checkin_time' )

    return render_to_response ( 'in_club.html', args )
