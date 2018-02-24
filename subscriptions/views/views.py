# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect

from django.core.context_processors import csrf

from database.args import create_args

from setup.models import Settings

from subscriptions.models import *

# Klienta modelis
from clients.models import Klienti

from datetime import timedelta, datetime


#============================================================
# !!!!! ABONEMENTI !!!!!
def subscription(request, back=False):
    args = create_args(request)
    if args['access'] == False:
        return redirect (Settings.objects.get( key = "access denied redirect" ).value)

    if args['loged_in'] == False:
        return redirect("/login/")

    args.update(csrf(request)) # ADD CSRF TOKEN

   # "return path" from this view
    if back == "edit":
        args['back'] = "/client/edit/"

    else:
        args['back'] = "/"

#    card_cost = int(Settings.objects.get( key = "client card price" ).value)
#    args['card'] = card_cost

    args['abonementi'] = AbonementType.objects.filter( position = 1, available = True )

    args['vienreiz'] = AbonementType.objects.filter( position = 2, available = True )

    args['special'] = AbonementType.objects.filter( position = 3, available = True )

    args['first_time'] = AbonementType.objects.filter(  position = 4, available = True )

    return render_to_response ( 'subscription_choise.html', args )


#============================================================
# !!!!! ABONEMENTA APMAKSA !!!!!
def subscription_payment(request):
    args = create_args(request)
    if args['access'] == False:
        return redirect (Settings.objects.get( key = "access denied redirect" ).value)

    if args['loged_in'] == False:
        return redirect("/login/")

    args.update(csrf(request)) # ADD CSRF TOKEN

   # Get Subscription Type from "Pirkt Abonementu" choise
    if request.POST:
        subscr_nr = int(request.POST.get('subscription', ''))
        args['chosen_subscr'] = AbonementType.objects.get( id = subscr_nr )

    return render_to_response ( 'subscription_payment.html', args )


#============================================================
# !!!!! ABONEMENTA PIRKŠANA !!!!!
def subscription_purchase(request):
    args = create_args(request)
    if args['access'] == False:
        return redirect (Settings.objects.get( key = "access denied redirect" ).value)

    if args['loged_in'] == False:
        return redirect("/login/")

   # Get Active client from COOKIE
    if "active_client" in request.COOKIES:
        try:
            c_id = int(request.COOKIES.get(str('active_client')))
            cli = Klienti.objects.get( id = c_id )

            if request.POST:
                subscr_nr = int(request.POST.get('subscription', ''))
                chosen_subscr = AbonementType.objects.get( id = subscr_nr )

                date_temp = datetime.now() + timedelta(days=30)
                if chosen_subscr.times:
                    new_subscr = Abonementi(client=cli, subscr=chosen_subscr, price=chosen_subscr.price, activate_before=date_temp, times_count=chosen_subscr.times_count)
                else:
                    new_subscr = Abonementi(client=cli, subscr=chosen_subscr, price=chosen_subscr.price, activate_before=date_temp)
                new_subscr.save()
        except:
            pass
    response = redirect("/")
    response.set_cookie( key='subscription_purchased', value="True", max_age=3 )
    return response

#============================================================
# !!!!! SUBSCRIPTION HISTORY !!!!!
def subscription_history(request):
    args = create_args(request)
    if args['access'] == False:
        return redirect (Settings.objects.get( key = "access denied redirect" ).value)

    if args['loged_in'] == False:
        return redirect("/login/")

    return render_to_response ( 'subscription_history.html', args )


#============================================================
# !!!!! ABONEMENTA IESLADĒŠANA !!!!!
def subscription_freeze(request):
    args = create_args(request)
    if args['access'] == False:
        return redirect (Settings.objects.get( key = "access denied redirect" ).value)

    if args['loged_in'] == False:
        return redirect("/login/")

    return render_to_response ( 'subscription_freeze.html', args )
