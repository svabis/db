# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect

from database.args import create_args

from setup.models import Settings

from clients.models import Klienti
from lockers.models import Skapji, Skapji_history

# import paginator
from database.paginator import Paginator
import math

#============================================================
# !!!!! Apmeklējumu vēsture !!!!!
def history(request, pageid = 1):
    args = create_args(request)
    if args['access'] == False:
        return redirect (Settings.objects.get( key = "access denied redirect" ).value)

    if args['loged_in'] == False:
        return redirect("/login/")

    results_per_page = int(Settings.objects.get( key = "search results on page" ).value)

    if "active_client" in request.COOKIES:
        c_id = int(request.COOKIES.get(str('active_client')))
        client = Klienti.objects.get( id = c_id )

    try:
        args['new_data'] = Skapji.objects.get( client = client )
    except:
        pass

    try:
        data = Skapji_history.objects.filter( client = client ).order_by('-checkin_time')

       # Paginate Search results
        if int(pageid) < 1: # negative page number --> 404
            return redirect ('/')

        pagecount = int(math.ceil( int(data.count()) / float( results_per_page ))) # integer identical to range by count

        if int(pageid) > pagecount and int(pageid) > 1: # pageid exceeds pagecount --> 404
            return redirect ('/')

        start_obj = int(pageid) * results_per_page - results_per_page # start from image NR
        end_obj = int(pageid) * results_per_page # end with image NR
        if end_obj > data.count(): # if end NR exceeds limit set it to end NR
            end_obj = data.count()

        args['paginator'] = Paginator( pagecount, pageid )
        args['data'] = data[start_obj:end_obj]
        args['pageid'] = int(pageid)

    except:
        pass
    return render_to_response ( 'lockers_history.html', args )

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
    args['data'] = Skapji.objects.all().order_by( 'checkin_time' )

    return render_to_response ( 'in_club.html', args )


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
