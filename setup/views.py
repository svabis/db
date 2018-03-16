# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect

from django.core.context_processors import csrf

from database.args import create_args

# Klientu statusi
from clients.models import Statusi

# Setingi
from setup.models import Settings, Apdrosinataji


def settings(request):
    args = create_args(request)
    if args['access'] == False:
        return redirect (Settings.objects.get( key = "access denied redirect" ).value)

    if args['loged_in'] == False:
        return redirect("/login/")

    args['active_tab_7'] = True

   # Apdrošinātāji
    args['insurance'] = Apdrosinataji.objects.all()

   # Klienti StatusType's
    args['status'] = Statusi.objects.all()

   # Main Settings
    args['settings'] = Settings.objects.all()

    return render_to_response ( 'settings.html', args )
