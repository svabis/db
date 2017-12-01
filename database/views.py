# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect

from django.core.context_processors import csrf

from database.args import create_args

from setup.models import Settings

# Klienta modelis
from klienti.models import Klienti


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


    if request.POST:
        client_card = int(request.POST.get('id', ''))
#        client = Klienti.objects.get( card_nr = client_card )
        client = Klienti.objects.get( id = client_card )

        args['abon_active'] = True

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# !!!!! INSERT CARD NOT FOUND E.T.C. !!!!!
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

#        id = int(request.POST.get('id', ''))
#        if id == "14083":
#            client = Klienti.objects.all()[0]
#            args['abon_active'] = True
#        if id == "uldis":
#            client = Klienti.objects.all()[0]
#            args['abon_active'] = True
#        if id == "1":
#            client = Klienti.objects.all()[2]
#            args['abon_active'] = True
#        if id == "2":
#            client = Klienti.objects.all()[3]
#        if id == "3":
#            client = Klienti.objects.all()[4]
#        if id == "klblok":
#            client = Klienti.objects.all()[2]
#            args['mesage'] = True
#            args['mesage_type'] = "error"
#            args['mesage_code_3'] = True
#        if id == "cblok":
#            client = Klienti.objects.all()[2]
#            args['mesage'] = True
#            args['mesage_type'] = "error"
#            args['mesage_code_2'] = True
#        if id == "er":
#            args['mesage'] = True
#            args['mesage_type'] = "error"
#            args['mesage_code_1'] = True

#        if id == "svabis" or  id == "20002":
#            client = Klienti.objects.get(id=18077)
#            args['mesage'] = True
#            args['mesage_type'] = "mesage"
#            args['mesage_code_4'] = True
#            args['abon_active'] = True

    if client != False:
        args['client'] = client

    response = render_to_response ( 'main_content.html', args )
#    response = rendirect ("/")
    try:
        response.set_cookie( key='active_client', value=client.id )
    except:
        response.delete_cookie('active_client')
    return response


#============================================================
# !!!!! ABONEMENTI !!!!!
def subscription(request):
    args = create_args(request)
    if args['access'] == False:
        return redirect (Settings.objects.get( key = "access denied redirect" ).value)

    return render_to_response ( 'subscription.html', args )


# !!!!! ABONEMENTA APMAKSA !!!!!
def subscription_payment(request):
    args = create_args(request)
    if args['access'] == False:
        return redirect (Settings.objects.get( key = "access denied redirect" ).value)

    return render_to_response ( 'subscription_payment.html', args )


# !!!!! ABONEMENTA IESLADĒŠANA !!!!!
def freeze_subscription(request):
    args = create_args(request)
    if args['access'] == False:
        return redirect (Settings.objects.get( key = "access denied redirect" ).value)

    return render_to_response ( 'freeze_subscription.html', args )


