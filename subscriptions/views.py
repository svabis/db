# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect

from django.core.context_processors import csrf

from database.args import create_args

from setup.models import Settings

from subscriptions.models import AbonementType
# Klienta modelis
#from clients.models import Klienti


#============================================================
# !!!!! ABONEMENTI !!!!!
def subscription(request):
    args = create_args(request)
    if args['access'] == False:
        return redirect (Settings.objects.get( key = "access denied redirect" ).value)

    args['abonementi'] = AbonementType.objects.filter( position = 1 )

    args['vienreiz'] = AbonementType.objects.filter( position = 2 )

    args['special'] = AbonementType.objects.filter( position = 3 )

    args['first_time'] = AbonementType.objects.filter(  position = 4 )

    return render_to_response ( 'subscription_choise.html', args )



# !!!!! ABONEMENTA APMAKSA !!!!!
def subscription_payment(request):
    args = create_args(request)
    if args['access'] == False:
        return redirect (Settings.objects.get( key = "access denied redirect" ).value)

    return render_to_response ( 'subscription_payment.html', args )



# !!!!! ABONEMENTA IESLADĒŠANA !!!!!
def subscription_freeze(request):
    args = create_args(request)
    if args['access'] == False:
        return redirect (Settings.objects.get( key = "access denied redirect" ).value)

    return render_to_response ( 'subscription_freeze.html', args )
