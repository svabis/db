# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect

from django.core.context_processors import csrf

from database.args import create_args

# Django useri
#from django.contrib.auth.models import User

from setup.models import Settings

# Abonementi
from subscriptions.models import *

# Klienta modelis
from clients.models import Klienti

from datetime import timedelta, datetime, date


def max_date(cli):
    subscriptions = Abonementi.objects.filter( client = cli, ended = False )
    activate_before_dates = []
    best_before_dates = []

   # savāc datumus
    for s in subscriptions:
        if s.active:
            best_before_dates.append( s.best_before )
        else:
            if isinstance( s.activate_before, datetime ) == True:
                activate_before_dates.append( s.activate_before )

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

    return max_date



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
#        if True:
        try:
            c_id = int(request.COOKIES.get(str('active_client')))
            cli = Klienti.objects.get( id = c_id )

           # POST
            if request.POST:
                args['today'] = datetime.now()
                max_d = max_date( cli )
                args['max_date'] = max_d

                args['client'] = cli

                f_start_str = request.POST.get('freeze_start', '')
                f_end_str = request.POST.get('freeze_end', '')

               # convert dates from string to datetime
                date_error = False
                try:
                    f_start_date = datetime.strptime( f_start_str, '%Y-%m-%d')
                except:
                    args['start_error'] = True
                    date_error = True
                try:
                    f_end_date = datetime.strptime( f_end_str, '%Y-%m-%d')
                except:
                    args['end_error'] = True
                    date_error = True

               # dates error
                if date_error == True:
                    return render_to_response ( 'subscription_freeze.html', args )

                if f_end_date.date() > max_d.date():  #(max_date( cli ) + timedelta(days=1)).date:
                    args['end_limit'] = True
                    return render_to_response ( 'subscription_freeze.html', args )

                d = (f_end_date - f_start_date).days
                args['days'] = d

               # freeze process
                subscr = Abonementi.objects.filter( client = cli, ended = False )

               # freeze client
                cli.frozen_from = f_start_date.date()
                cli.frozen_until = f_end_date.date()
                if cli.frozen_from <= date.today():
                    cli.frozen = True
                cli.save()

                for s in subscr:
                    if s.active:
                        new_freeze = Abonementu_Iesalde( user=args['username'], client=cli, subscr=s, best_before=s.best_before)
                        new_freeze.save()
                        s.best_before = s.best_before + timedelta(days = d)
                    else:
                        new_freeze = Abonementu_Iesalde( user=args['username'], client=cli, subscr=s, activate_before=s.activate_before)
                        new_freeze.save()
                        s.activate_before = s.activate_before + timedelta(days=d)
                    s.save()

           # GET
            else:
                args['today'] = datetime.now()
                args['max_date'] = max_date( cli )
                args['client'] = cli
        except:
            pass
    return render_to_response ( 'subscription_freeze.html', args )
