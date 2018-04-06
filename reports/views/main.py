# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect

from django.core.context_processors import csrf

from database.args import create_args

# Klientu statusi
from clients.models import Statusi

# Setingi
from setup.models import Settings

# Abonementi
from subscriptions.models import AbonementType

from datetime import datetime #, timedelta, date, time


# !!!!! Atskaites !!!!!
def main(request):
    args = create_args(request)
    if args['access'] == False:
        return redirect (Settings.objects.get( key = "access denied redirect" ).value)
    if args['loged_in'] == False:
        return redirect("/login/")
    if args['admin'] != True:
        return redirect("/login/")

    args.update(csrf(request)) # ADD CSRF TOKEN

    args['active_tab_5'] = True

    args['ab'] = AbonementType.objects.filter( available=True ).order_by('title')

    args['today'] = datetime.now()

    return render_to_response ( 'reports_main.html', args )
