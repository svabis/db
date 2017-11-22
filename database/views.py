# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect

#from django.contrib import auth # autorisation library
#from django.contrib.auth.models import User, Group

from django.core.context_processors import csrf

from database.args import create_args

# Klienta modelis
from klienti.models import Klienti


# !!!!! Clear ID !!!!!
def clear_id(request):
    response = redirect ('/')
    response.delete_cookie('active_client')
    return response


# !!!!! MAIN VIEW !!!!!
def main(request):
    args = create_args(request)
    args.update(csrf(request))      # ADD CSRF TOKEN

    args['active_tab_1'] = True

    if "active_client" in request.COOKIES:
        try:
            c_id = int(request.COOKIES.get(str('active_client')))
            client = Klienti.objects.get( id = c_id )
        except:
            pass
    else:
        client = False


    if request.POST:
        id = request.POST.get('id', '')
        if id == "14083":
            client = Klienti.objects.all()[0]
            args['abon_active'] = True
        if id == "uldis":
            client = Klienti.objects.all()[0]
            args['abon_active'] = True
        if id == "1":
            client = Klienti.objects.all()[2]
            args['abon_active'] = True
        if id == "2":
            client = Klienti.objects.all()[3]
        if id == "3":
            client = Klienti.objects.all()[4]
        if id == "klblok":
            client = Klienti.objects.all()[2]
            args['error'] = True
            args['error_code_3'] = True
        if id == "cblok":
            client = Klienti.objects.all()[2]
            args['error'] = True
            args['error_code_2'] = True
        if id == "er":
            args['error'] = True
            args['error_code_1'] = True
        if id == "svabis":
            args['abon_active'] = True
            client = Klienti.objects.all()[1]

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
# !!!!! SKAPĪŠI !!!!!
def locker(request):
    args = create_args(request)

    if "active_client" in request.COOKIES:
        c_id = int(request.COOKIES.get(str('active_client')))
        client = Klienti.objects.get( id = c_id )
    else:
        redirect ("/")

    lockers = []

    if client.gender == "V":
       for i in range(0,105):
           lockers.append(i+1);
    else:
       for i in range(0,176):
           lockers.append(i+1);

    args['lockers'] = lockers
    args['gender'] = client.gender

    return render_to_response ( 'locker.html', args )


#============================================================
# !!!!! ABONEMENTI !!!!!
def subscription(request):
    args = create_args(request)
    return render_to_response ( 'subscription.html', args )
