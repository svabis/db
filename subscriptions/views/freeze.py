# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect

from django.core.context_processors import csrf

from database.args import create_args

# Django useri
from django.contrib.auth.models import User

from setup.models import Settings

from subscriptions.models import *

# Klienta modelis
from clients.models import Klienti

from datetime import timedelta, datetime


#============================================================
# !!!!! ABONEMENTA IESLADĒŠANA !!!!!
def subscription_freeze(request):
    args = create_args(request)
    if args['access'] == False:
        return redirect (Settings.objects.get( key = "access denied redirect" ).value)

    if args['loged_in'] == False:
        return redirect("/login/")

    args.update(csrf(request)) # ADD CSRF TOKEN

   # Get Active client from COOKIE
    if "active_client" in request.COOKIES:
        try:
            c_id = int(request.COOKIES.get(str('active_client')))
            cli = Klienti.objects.get( id = c_id )

            subscriptions = Abonementi.objects.filter( client = cli, ended = False )

            activated = []
            activate_before_dates = []
            best_before_dates = []

           # savāc datumus
            for s in subscriptions:
                activated.append( s.active )
                if s.active:
                    best_before_dates.append( s.best_before )
                else:
                    if isinstance( s.activate_before, datetime ) == True:
                        activate_before_dates.append( s.activate_before )

            args['active'] = activated
            args['activate'] = activate_before_dates
            args['best'] = best_before_dates

           # nosaka max datumus AKTIVĒT LĪDZ
            if len( activate_before_dates ) > 1:
                max_activate = max(activate_before_dates)
            elif len( activate_before_dates ) == 1:
                max_activate = activate_before_dates[0]
            else:
                max_activate = []

           # nosaka max datumus DERĪGS LĪDZ
            if len( best_before_dates ) > 1:
                max_best_before = max(best_before_dates)
            elif len( best_before_dates ) == 1:
                max_best_before = best_before_dates[0]
            else:
                max_best_before = []

           # saliek max_1 un max_2
            max_dates = []
            if isinstance( max_activate, datetime ) == True:
                max_dates.append(max_activate)
            if isinstance( max_best_before, datetime ) == True:
                max_dates.append(max_best_before)

           # meklē jaunāko ja ir...
            if len( max_dates ) > 1:
                max_date = max(max_dates)
            elif len( max_dates ) == 1:
                max_date = max_dates[0]
            else:
                max_date = []

            args['activatemax'] = max_activate
            args['bestmax'] = max_best_before

            args['maxm'] = max_dates

            args['today'] = datetime.now()
            args['max_date'] = max_date

            args['client'] = cli
        except:
            pass
    return render_to_response ( 'subscription_freeze.html', args )
