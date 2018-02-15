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
def subscription(request, back=False):
    args = create_args(request)
    if args['access'] == False:
        return redirect (Settings.objects.get( key = "access denied redirect" ).value)

    if args['loged_in'] == False:
        return redirect("/login/")

   # return path from this view
    if back == "edit":
        args['back'] = "/client/edit/"

    else:
        args['back'] = "/"

    card_cost = int(Settings.objects.get( key = "client card price" ).value)

    args['card'] = card_cost

    args['abonementi'] = AbonementType.objects.filter( position = 1, available = True )

    args['vienreiz'] = AbonementType.objects.filter( position = 2, available = True )

    args['special'] = AbonementType.objects.filter( position = 3, available = True )

    args['first_time'] = AbonementType.objects.filter(  position = 4, available = True )

    return render_to_response ( 'subscription_choise.html', args )



# !!!!! ABONEMENTA APMAKSA !!!!!
def subscription_payment(request):
    args = create_args(request)
    if args['access'] == False:
        return redirect (Settings.objects.get( key = "access denied redirect" ).value)

    if args['loged_in'] == False:
        return redirect("/login/")

    return render_to_response ( 'subscription_payment.html', args )



# !!!!! ABONEMENTA IESLADĒŠANA !!!!!
def subscription_freeze(request):
    args = create_args(request)
    if args['access'] == False:
        return redirect (Settings.objects.get( key = "access denied redirect" ).value)

    if args['loged_in'] == False:
        return redirect("/login/")

    return render_to_response ( 'subscription_freeze.html', args )
