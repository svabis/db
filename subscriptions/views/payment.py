# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect

from django.core.context_processors import csrf

from database.args import create_args

# Django useri
#from django.contrib.auth.models import User

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
        temp_dep = str( Deposit.objects.filter( d_client = cli ).order_by('-d_date')[0].d_remain )
        args['deposit'] = temp_dep.replace(",", ".")
    except:
        args['deposit'] = 0

   # Get Subscription Type from "Pirkt Abonementu" choise
    if request.POST:

        multi = int(request.POST.get('multiplicator', ''))
        args['multi'] = multi

        subscr_nr = int(request.POST.get('subscription', ''))
        chosen_sub = AbonementType.objects.get( id = subscr_nr )
        args['chosen_subscr'] = chosen_sub

        args['subscr_price'] = str(chosen_sub.price * multi).replace(",", ".")

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
               # read POST data
                subscr_nr = int( request.POST.get('subscription', '') )
                chosen_subscr = AbonementType.objects.get( id = subscr_nr )
                multi = int( request.POST.get('multiplicator', '') )

                discount_price = request.POST.get('id_price_to_pay', '').split(" ")[1]
                new_deposit_remain = float( request.POST.get('deposit_remain', '').split(" ")[1] )
                from_deposit = float( request.POST.get('deposit_used', '').split(" ")[1] )
                gift_card = float( request.POST.get('id_gift_card_ammount', '').split(" ")[1] )
                transfer_chk = request.POST.get('transfer_chk', '')
                final = float( request.POST.get('id_total_price').split(" ")[1] )
                insurance_comp = request.POST.get('insurance_comp', '')
                insurance_cash = float( request.POST.get('id_insurance_ammount').split(" ")[1] )

               # find last client deposit amount
                try:
                    old_deposit_remain = float( Deposit.objects.filter( d_client = cli ).order_by('-d_date')[0].d_remain ) # to test deposit if was
                except:
                    old_deposit_remain = float( 0 )

               # deposit remain is diferent
                save_deposit = False
                if new_deposit_remain != old_deposit_remain:
                   # depozīta atlikums
                    if new_deposit_remain > 0:
                       if insurance_cash > 0 and gift_card > 0:
                            new_deposit = Deposit( d_user = args['username'], d_client = cli, d_reason="Dāvanu karte + Apdrošināšana", d_added = new_deposit_remain, d_remain = new_deposit_remain )
                            save_deposit = True
                       elif insurance_cash > 0:
                            new_deposit = Deposit( d_user = args['username'], d_client = cli, d_reason="Apdrošināšana", d_added = new_deposit_remain, d_remain = new_deposit_remain )
                            save_deposit = True
                       elif gift_card > 0:
                            new_deposit = Deposit( d_user = args['username'], d_client = cli, d_reason="Dāvanu karte", d_added = new_deposit_remain, d_remain = new_deposit_remain )
                            save_deposit = True
                      # depozīts izmantots
                       else:
                            new_deposit = Deposit( d_user = args['username'], d_client = cli, d_reason="Izmantots pirkumam", d_added = 0, d_remain = new_deposit_remain )
                    if new_deposit_remain == 0:
                       new_deposit = Deposit( d_user = args['username'], d_client = cli, d_reason="Izmantots pirkumam", d_added = 0, d_remain = new_deposit_remain )
                    new_deposit.save()

               # client notes
                notes = cli.notes
                new_notes = request.POST.get('notes', '')
                if notes != new_notes:
                    cli.notes = new_notes
                    cli.save()

               # if first time --> check client.first = True
                if Abonementi.objects.filter( client = cli ).count() == 0:
                    cli.first = True
                    cli.save()

               # activation time for purchased subscription (including multiple)
                temp_date = datetime.now() + timedelta( days = 30 * chosen_subscr.activate_before * multi )

# !!!!!!!!!!!!!!!!!!
                create_count = 0
                while create_count != multi:
                   # create Abonementi object
                    if chosen_subscr.times:
                        new_subscr = Abonementi( user=system_user, client=cli, subscr=chosen_subscr, price=chosen_subscr.price, activate_before=temp_date, times_count=chosen_subscr.times_count)
                    else:
                        new_subscr = Abonementi( user=system_user, client=cli, subscr=chosen_subscr, price=chosen_subscr.price, activate_before=temp_date)
                   # save new Abonementi object
                    new_subscr.save()
                    create_count += 1
# !!!!!!!!!!!!!!!!!!

               # ===================================
               # PREPARING TO CREATE PURCHASE OBJECT
                if insurance_comp == "":
                    if save_deposit:
                        new_purchase = Abonementu_Apmaksa( user=system_user, client=cli, subscr=new_subscr, full_price=chosen_subscr.price*multi, discount_price=discount_price, count=multi,
                                                   from_deposit=from_deposit, from_gift_card=gift_card, insurance_cash=insurance_cash,
                                                   transfer=transfer_chk, final_price=final, deposit=new_deposit )
                    else:
                        new_purchase = Abonementu_Apmaksa( user=system_user, client=cli, subscr=new_subscr, full_price=chosen_subscr.price*multi, discount_price=discount_price, count=multi,
                                                   from_deposit=from_deposit, from_gift_card=gift_card, insurance_cash=insurance_cash,
                                                   transfer=transfer_chk, final_price=final )
                else:
                    insurance_comp = Apdrosinataji.objects.get( id = int(insurance_comp) )
                    if save_deposit:
                        new_purchase = Abonementu_Apmaksa( user=system_user, client=cli, subscr=new_subscr, full_price=chosen_subscr.price*multi, discount_price=discount_price, count=multi,
                                                   from_deposit=from_deposit, from_gift_card=gift_card, insurance=insurance_comp, insurance_cash=insurance_cash,
                                                   transfer=transfer_chk, final_price=final, deposit=new_deposit )
                    else:
                        new_purchase = Abonementu_Apmaksa( user=system_user, client=cli, subscr=new_subscr, full_price=chosen_subscr.price*multi, discount_price=discount_price, count=multi,
                                                   from_deposit=from_deposit, from_gift_card=gift_card, insurance=insurance_comp, insurance_cash=insurance_cash,
                                                   transfer=transfer_chk, final_price=final )
                new_purchase.save()
#        except:
#            pass

    response = redirect("/")
    response.set_cookie( key='subscription_purchased', value="True", max_age=3 )
    return response
