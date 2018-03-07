# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect

from django.core.context_processors import csrf

from database.args import create_args

# Django useri
from django.contrib.auth.models import User

from setup.models import Settings, Apdrosinataji

from subscriptions.models import *

# Klienta modelis
from clients.models import Klienti, Deposit

from datetime import timedelta, datetime, date


#============================================================
# !!!!! ABONEMENTA APMAKSA !!!!!
def subscription_payment(request):
    args = create_args(request)
    if args['access'] == False:
        return redirect (Settings.objects.get( key = "access denied redirect" ).value)

    if args['loged_in'] == False:
        return redirect("/login/")

    args.update(csrf(request)) # ADD CSRF TOKEN

    args['insurance'] = Apdrosinataji.objects.filter( visible = True )

   # Get Active client from COOKIE
    if "active_client" in request.COOKIES:
        try:
            c_id = int(request.COOKIES.get(str('active_client')))
            cli = Klienti.objects.get( id = c_id )

            args['client'] = cli
        except:
            return ("/")

    try:
        temp_dep = str( Deposit.objects.filter( d_client = cli ).order_by('-d_date')[0].d_amount )
        args['deposit'] = temp_dep.replace(",", ".")
    except:
        args['deposit'] = 0

   # Get Subscription Type from "Pirkt Abonementu" choise
    if request.POST:
        subscr_nr = int(request.POST.get('subscription', ''))
        chosen_sub = AbonementType.objects.get( id = subscr_nr )
        args['chosen_subscr'] = chosen_sub

        args['subscr_price'] = str(chosen_sub.price).replace(",", ".")

       # Ja nav "speciālais" abonements...
        if chosen_sub.discount == True:
             args['discount_available'] = "true" # for JS
        else:
             args['discount_available'] = "false" # for JS

       # Student, Disabled, Elderly discount CHECK
        today_date = datetime.now().date()
        sed_discount = 0
        if cli.student == True:
            if isinstance( cli.student_until, date ) == True:
                if cli.student_until > today_date:
                    sed_discount = True
        if cli.disabled == True:
            if isinstance( cli.disabled_until, date ) == True:
                if cli.disabled_until > today_date:
                    sed_discount = True
        if cli.elderly == True:
            sed_discount = True
       # set 10% discount
        if sed_discount == True:
            sed_discount = 10

       # chose highest discount
        if float(cli.status.status_discount) > float(sed_discount):
            args['initial_discount'] = cli.status.status_discount
        else:
            args['initial_discount'] = sed_discount

    return render_to_response ( 'subscription_payment.html', args )



#============================================================
# !!!!! ABONEMENTA PIRKŠANA !!!!!
def subscription_purchase(request):
    args = create_args(request)
    if args['access'] == False:
        return redirect (Settings.objects.get( key = "access denied redirect" ).value)

    if args['loged_in'] == False:
        return redirect("/login/")

    system_user = args['username']

   # Get Active client from COOKIE
    if "active_client" in request.COOKIES:
        if True:
#        try:
            c_id = int(request.COOKIES.get(str('active_client')))
            cli = Klienti.objects.get( id = c_id )

            if request.POST:
                subscr_nr = int( request.POST.get('subscription', '') )
                chosen_subscr = AbonementType.objects.get( id = subscr_nr )

                discount_price = request.POST.get('id_price_to_pay', '').split(" ")[1]

#                if True:
                try:
                    temp = float( Deposit.objects.filter( d_client = cli ).order_by('-d_date')[0].d_amount ) # to test deposit if was
                    remain_deposit = float( request.POST.get('deposit_remain', '').split(" ")[1] )

                    new_deposit = Deposit( d_user = args['username'], d_client = cli, d_amount = remain_deposit )
                    new_deposit.save()
                except:
                    pass

                notes = cli.notes
                new_notes = request.POST.get('notes', '')
                if notes != new_notes:
                    cli.notes = new_notes
                    cli.save()

                if chosen_subscr.first_time == True:
                    cli.first = True
                    cli.save()

               # create Abonementi object
                temp_date = datetime.now() + timedelta( days=30*chosen_subscr.activate_before )
                if chosen_subscr.times:
                    new_subscr = Abonementi( user=system_user, client=cli, subscr=chosen_subscr, price=chosen_subscr.price, activate_before=temp_date,
                                            times_count=chosen_subscr.times_count)
                else:
                    new_subscr = Abonementi( user=system_user, client=cli, subscr=chosen_subscr, price=chosen_subscr.price, activate_before=temp_date)
                new_subscr.save()

               # PREPARING TO CREATE PURCHASE OBJECT

                from_deposit = float( request.POST.get('deposit_used', '').split(" ")[1] )
                gift_card = float( request.POST.get('id_gift_card_ammount', '').split(" ")[1] )
                cash_chk = request.POST.get('cash_chk', '')
                credit_card_chk = request.POST.get('credit_card_chk', '')
                transfer_chk = request.POST.get('transfer_chk', '')
                final = float( request.POST.get('id_total_price').split(" ")[1] )

                insurance_comp = request.POST.get('insurance_comp', '')
                insurance_cash = float( request.POST.get('id_insurance_ammount').split(" ")[1] )

                if insurance_comp == "":
                    new_purchase = Abonementu_Apmaksa( user=system_user, client=cli, subscr=new_subscr, full_price=chosen_subscr.price, discount_price=discount_price,
                                                   from_deposit=from_deposit, from_gift_card=gift_card, insurance_cash=insurance_cash,
                                                   cash=cash_chk, card=credit_card_chk, transfer=transfer_chk, final_price=final )
                else:
                    insurance_comp = Apdrosinataji.objects.get( id = int(insurance_comp) )
                    new_purchase = Abonementu_Apmaksa( user=system_user, client=cli, subscr=new_subscr, full_price=chosen_subscr.price, discount_price=discount_price,
                                                   from_deposit=from_deposit, from_gift_card=gift_card, insurance=insurance_comp, insurance_cash=insurance_cash,
                                                   cash=cash_chk, card=credit_card_chk, transfer=transfer_chk, final_price=final )
                new_purchase.save()
#        except:
#            pass

    response = redirect("/")
    response.set_cookie( key='subscription_purchased', value="True", max_age=3 )
    return response
