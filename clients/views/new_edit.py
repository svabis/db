# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect

from django.core.context_processors import csrf

#from django.db.models import Q # search in multiple columns

from clients.forms import KlientsForm
from clients.models import Klienti, Blacklist, Deposit

from subscriptions.models import Abonementi

from setup.models import Settings

from database.args import create_args

#from clients.paginator import Paginator  # import paginator
#import math # for rounding up Page Counter


# !!!!! NEW CLIENT !!!!!
def new_client(request):
    args = create_args(request)
    if args['access'] == False:
        return redirect (Settings.objects.get( key = "access denied redirect" ).value)

    if args['loged_in'] == False:
        return redirect("/login/")

    args.update(csrf(request)) # ADD CSRF TOKEN
   # Settings
    args['card_string'] = Settings.objects.get( key = "card string" ).value

   # Created form POST
    if request.POST:
        form = KlientsForm( request.POST, request.FILES )

        if form.is_valid():
#            card_nr = str( request.POST.get('card_nr', '') )
#            card_nr_array = Klienti.objects.all().exclude( card_nr = "" ).values('card_nr')

# !!!!!!!!!!!!!!!!!!!!!!!!!!
# !!!!! CARD TEST HERE !!!!!
# !!!!!!!!!!!!!!!!!!!!!!!!!!

            new_client = form.save()
            response = redirect("/")
            response.set_cookie( key='active_client', value=new_client.id )
            response.set_cookie( key='new_client', value="True", max_age=3 )
            return response
        else:
            args['form'] = form
            return render_to_response ( 'clients_new_client.html', args )

    args['form'] = KlientsForm

    args['active_tab_2'] = True
    return render_to_response ( 'clients_new_client.html', args )


#==================================================================
# !!!!! EDIT CLIENT !!!!!
def edit_client(request):
    args = create_args(request)
    if args['access'] == False:
        return redirect (Settings.objects.get( key = "access denied redirect" ).value)

    if args['loged_in'] == False:
        return redirect("/login/")

    args.update(csrf(request)) # ADD CSRF TOKEN
   # Settings
    args['card_string'] = Settings.objects.get( key = "card string" ).value

   # Edited form POST
    if request.POST:
        c_id = int(request.COOKIES.get(str('active_client')))
        client = Klienti.objects.get( id = c_id  )
        form = KlientsForm( request.POST, request.FILES, instance = client )

        if form.is_valid():
            form.save()
            response = redirect("/")
            response.set_cookie( key='edit_client', value="True", max_age=3 )
            return response
        else:
            args['form'] = form
            args['client'] = client
            return render_to_response ( 'clients_edit_client.html', args )

   # LOAD ACTIVE CLIENT FROM COOKIES
    if "active_client" in request.COOKIES:
        try:
            c_id = int(request.COOKIES.get(str('active_client')))
            client = Klienti.objects.get( id = c_id )
            args['client'] = client

            args['bl_data'] = Blacklist.objects.filter( bl_client = client )

            form = KlientsForm( instance = client )
            args['form'] = form

            args['active_tab_3'] = True

            try:
                args['deposit_amount'] = Deposit.objects.filter( d_client = client ).order_by('-d_date')[0]
            except:
                args['deposit_amount'] = 0

            f_temp = Abonementi.objects.filter( client = client, ended = False )
            if f_temp.count() == 0:
                args['freeze_disable'] = True
        except:
            pass
    else:
        return redirect ("/")

    return render_to_response ( 'clients_edit_client.html', args )
