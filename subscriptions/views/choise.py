# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect

from django.core.context_processors import csrf

from database.args import create_args

# Django useri
#from django.contrib.auth.models import User

from setup.models import Settings

from subscriptions.models import *

# Klienta modelis
from clients.models import Klienti

#from datetime import timedelta, datetime


#============================================================
# !!!!! ABONEMENTI !!!!!
def subscription(request, back=False):
    args = create_args(request)
    if args['access'] == False:
        return redirect (Settings.objects.get( key = "access denied redirect" ).value)

    if args['loged_in'] == False:
        return redirect("/login/")

   # Get Active client from COOKIE
    if "active_client" in request.COOKIES:
#        if True:
        try:
            c_id = int(request.COOKIES.get(str('active_client')))
            cli = Klienti.objects.get( id = c_id )
        except:
            cli = False

    args.update(csrf(request)) # ADD CSRF TOKEN

   # "return path" from this view
    if back == "edit":
        args['back'] = "/client/edit/"
    else:
        args['back'] = "/"

    args['abonementi1'] = AbonementType.objects.filter( position = 1, position1 = 1, available = True )
    args['abonementi2'] = AbonementType.objects.filter( position = 1, position1 = 2, available = True )
    args['abonementi3'] = AbonementType.objects.filter( position = 1, position1 = 3, available = True )

    args['special'] = AbonementType.objects.filter( position = 3, available = True )

    if cli != False:
        if cli.first:
            args['first_time'] = AbonementType.objects.filter(  position = 4, available = True ).exclude( first_time = True )
        else:
            args['first_time'] = AbonementType.objects.filter(  position = 4, available = True )

        if Abonementi.objects.filter( client=cli, ended = False ).count() > 0:
            args['vienreiz'] = AbonementType.objects.filter( position = 2, available = True )
        else:
            args['vienreiz'] = AbonementType.objects.filter( position = 2, available = True ).exclude( position1 = 0 )

    return render_to_response ( 'subscription_choise.html', args )
