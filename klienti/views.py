# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect

from django.contrib import auth # autorisation library
from django.contrib.auth.models import User, Group

from django.core.context_processors import csrf

from klienti.models import Klienti

from klienti.forms import KlientsForm

from database.args import create_args


# !!!!! Redirect UP !!!!!
def main(request):
    return redirect('/')



# !!!!! NEW CLIENT !!!!!
def new_client(request):
    args = {}

    args.update(csrf(request)) # ADD CSRF TOKEN
    args['form'] = KlientsForm

    args['active_tab_2'] = True
    return render_to_response ( 'kli_new_client.html', args )



# !!!!! EDIT CLIENT !!!!!
def edit_client(request):
    args = create_args(request)
    args.update(csrf(request)) # ADD CSRF TOKEN

   # LOAD ACTIVE CLIENT FROM COOKIES
    if "active_client" in request.COOKIES:
        try:
            c_id = int(request.COOKIES.get(str('active_client')))
            client = Klienti.objects.get( id = c_id )
            args['client'] = client

            form = KlientsForm( instance = client )
            args['form'] = form

            args['active_tab_3'] = True
        except:
            return redirect ("/")

    else:
        return redirect ("/")

    return render_to_response ( 'kli_edit_client.html', args )
