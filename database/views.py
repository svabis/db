# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect

# multiple objects returned
from django.core.exceptions import MultipleObjectsReturned

from django.core.context_processors import csrf

from database.args import create_args

from setup.models import Settings

# Klienta modelis
from clients.models import Klienti, Deposit

# Skapīši modelis
from lockers.models import Skapji, Skapji_history

# Abonementi
from subscriptions.models import Abonementi

# Tools
from database.tools import ActiveSubscription, SubscriptionEnd


# !!!!! Clear ID !!!!!
def clear_id(request):
    args = create_args(request)
    if args['access'] == False:
        return redirect (Settings.objects.get( key = "access denied redirect" ).value)

    response = redirect ('/')
    response.delete_cookie('active_client')

    response.delete_cookie('edit_client')
    response.delete_cookie('new_client')
    return response


#===============================================================================
# !!!!! MAIN VIEW !!!!!
def main(request):
    args = create_args(request)
    if args['access'] == False:
        return redirect (Settings.objects.get( key = "access denied redirect" ).value)

    if args['loged_in'] == False:
        return redirect("/login/")

    card_scanned = False

    args.update(csrf(request))      # ADD CSRF TOKEN

   # SETTINGS
    args['woman_locker_color'] = Settings.objects.get( key = "woman locker color" ).value
    args['man_locker_color'] = Settings.objects.get( key = "man locker color" ).value
    args['card_string'] = Settings.objects.get( key = "card string" ).value

    args['active_tab_1'] = True

   # New client created
    if "new_client" in request.COOKIES:
        args['new_client'] = True
   # Client Edited
    if "edit_client" in request.COOKIES:
        args['edit_client'] = True
   # Subscription purchased
    if "subscription_purchased" in request.COOKIES:
        args['subscription_purchased'] = True
   # Notes updated
    if "notes_updated" in request.COOKIES:
        args['notes_updated'] = True

   # Get Active client from COOKIE
    if "active_client" in request.COOKIES:
        try:
            c_id = int(request.COOKIES.get(str('active_client')))
            client = Klienti.objects.get( id = c_id )
        except:
           # if client object listed in COOKIE is not available anymore
            client = False
   # if no COOKIE
    else:
        client = False

   # Card scanned
    if request.POST:
        try:
            client_card = str(request.POST.get('id', ''))
           # may be multiple objects
            client = Klienti.objects.get( card_nr = client_card )
        except:
           # Klients nav atrasts
            args['message'] = True
            args['message_type'] = "error"
            args['message_code_1'] = True
            client = False

       # Data received from card scanner
        card_scanned = True

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# !!!!!    "mesages displayed"    !!!!!
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    if client != False:
#    try:
      # Karte bloķēta
        if client.card_blocked == True:
            args['message'] = True
            args['message_type'] = "message"
            args['message_code_2'] = True

       # Karte melnajā sarakstā
        if client.client_blocked == True:
            args['message'] = True
            args['message_type'] = "message"
            args['message_code_3'] = True

       # Aktīva iesalde
        if client.frozen == True:
            args['message'] = True
            args['message_type'] = "message"
            args['message_code_5'] = True

       # Klienta status ir mainījies
        if client.status_changed != False: #True:
            args['message'] = True
            args['message_type'] = "message"
            args['message_code_4'] = True
           # save changes (status changed)
            client.status_changed = False
            client.save()

#    except:
#        pass
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    if client != False:
        args['client'] = client

       # dpozīts
        try:
            args['deposit_amount'] = Deposit.objects.filter( d_client = client ).order_by('-d_date')[0]
        except:
            args['deposit_amount'] = 0

       # Skapīša info
        try:
           # Skapītis piešķirts
            args['client_locker'] = Skapji.objects.get( client = client )
            args['checked'] = True
        except MultipleObjectsReturned:
           # Gļux --> Klients ir vairākos skapīšos ???
            sk = Skapji.objects.filter( client = client )
            temp_c = 0
            for s in sk.count():
                if temp_c != 0:
                    s.delete()
                temp_c += 1

            args['client_locker'] = sk[0]
            args['checked'] = True
        except:
           # klients nav iečekojies
            args['checked'] = False

       # Pēdējais apmeklējums
        try:
            last_visit = Skapji_history.objects.filter( client = client ).order_by('-checkout_time')[0]
            args['last_visit'] = last_visit.checkout_time
        except:
            args['no_visit_history'] = True

        args['sub_count'] = Abonementi.objects.filter( client = client, ended = False ).count()

       # ABONEMENTU ENDED TESTU ŠEIT...
        SubscriptionEnd( client )

       # ABONEMENTU APSTRĀDES ALGORITMS
        check = ActiveSubscription( client )
        args['abon_active'] = check.exists
        if check.exists:
            args['active_subscription'] = check.active

    response = render_to_response ( 'main_content.html', args )

    if card_scanned:
        response.delete_cookie('search_client')

    try:
        response.set_cookie( key='active_client', value=client.id )
    except:
        response.delete_cookie('active_client')
    return response



#===============================================================================
# !!!!! Update Client Notes !!!!!
def update_notes(request):
    args = create_args(request)
    if args['access'] == False:
        return redirect (Settings.objects.get( key = "access denied redirect" ).value)

   # Get Active client from COOKIE
    if "active_client" in request.COOKIES:
        try:
            c_id = int(request.COOKIES.get(str('active_client')))
            client = Klienti.objects.get( id = c_id )
            if request.POST:
                new_notes = request.POST.get('notes', '')

                client.notes = new_notes
                client.save()

                response = redirect("/")
                response.set_cookie( key='notes_updated', value="True", max_age=3 )
                return response
        except:
            pass

    return redirect("/")
