# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect

from django.core.context_processors import csrf

from database.args import create_args

# Klientu statusi
from clients.models import Statusi

# Setingi
from setup.models import Settings, Apdrosinataji


# !!!!! Settings !!!!!
def settings(request):
    args = create_args(request)
    if args['access'] == False:
        return redirect (Settings.objects.get( key = "access denied redirect" ).value)

    if args['loged_in'] == False:
        return redirect("/login/")

    if args['admin'] != True:
        return redirect("/login/")

    args['active_tab_7'] = True
    args['setup_tab_1'] = True

   # Main Settings
    args['settings'] = Settings.objects.all().order_by('key')

    return render_to_response ( 'settings.html', args )


# !!!!! Statusi !!!!!
def client_status(request):
    args = create_args(request)
    if args['access'] == False:
        return redirect (Settings.objects.get( key = "access denied redirect" ).value)

    if args['loged_in'] == False:
        return redirect("/login/")

    if args['admin'] != True:
        return redirect("/login/")

    args['active_tab_7'] = True
    args['setup_tab_4'] = True

   # Klienti Statusi
    args['status'] = Statusi.objects.all()

    return render_to_response ( 'settings.html', args )


# !!!!! Apdrošināšanas !!!!!
def insurance(request):
    args = create_args(request)
    if args['access'] == False:
        return redirect (Settings.objects.get( key = "access denied redirect" ).value)

    if args['loged_in'] == False:
        return redirect("/login/")

    if args['admin'] != True:
        return redirect("/login/")

    args['active_tab_7'] = True
    args['setup_tab_3'] = True

   # Apdrošinātāji
    args['insurance'] = Apdrosinataji.objects.all()

    return render_to_response ( 'settings.html', args )

