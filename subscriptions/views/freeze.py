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

            subscriptions = Abonementi.objects.filter( client = cli, ended = False ).order_by('-purchase_date')

            if subscriptions.count() == 1:
                args['subscription'] = Abonementi.objects.get( client = cli, ended = False )

            args['client'] = cli
            args['subscriptions'] = subscriptions
            args['sub_count'] = subscriptions.count()
        except:
            pass
    return render_to_response ( 'subscription_freeze.html', args )
