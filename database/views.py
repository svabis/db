# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect

from django.core.context_processors import csrf

from database.args import create_args

from setup.models import Settings

# Klienta modelis
from clients.models import Klienti


# !!!!! Clear ID !!!!!
def clear_id(request):
    response = redirect ('/')
    response.delete_cookie('active_client')

    response.delete_cookie('edit_client')
    response.delete_cookie('new_client')
    return response


# !!!!! MAIN VIEW !!!!!
def main(request):
    args = create_args(request)
    if args['access'] == False:
        return redirect (Settings.objects.get( key = "access denied redirect" ).value)

    args.update(csrf(request))      # ADD CSRF TOKEN

    args['active_tab_1'] = True

    args['card_string'] = Settings.objects.get( key = "card string" ).value

   # New client created
    if "new_client" in request.COOKIES:
        args['new_client'] = True
   # Client Edited
    if "edit_client" in request.COOKIES:
        args['edit_client'] = True

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
        client_card = int(request.POST.get('id', ''))
        try:
#            client = Klienti.objects.get( card_nr = client_card )
            client = Klienti.objects.get( id = client_card )

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# !!!!! Modal apvienojums, vai dalījums ? !!!!!
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

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

           # Klienta status ir mainījies
            if client.status_changed == True:
                 args['message'] = True
                 args['message_type'] = "message"
                 args['message_code_4'] = True

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# !!!!!   ABONEMENTU APSTRĀDES ALGORITMS   !!!!!
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            args['abon_active'] = True # pagaidām bez algoritma, 1-scan card=lockers, 2-atgriežoties no citas sadaļas=subscription

        except:
           # Klients nav atrasts
            args['message'] = True
            args['message_type'] = "error"
            args['message_code_1'] = True

    if client != False:
        args['client'] = client

    response = render_to_response ( 'main_content.html', args )
#    response = rendirect ("/") # domāts ja strādā ar cookies, lai disable refresh iespēju iekš lapas
    try:
        response.set_cookie( key='active_client', value=client.id )
    except:
        response.delete_cookie('active_client')
    return response
