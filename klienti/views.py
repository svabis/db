# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect

from django.contrib import auth # autorisation library
from django.contrib.auth.models import User, Group

from django.core.context_processors import csrf

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
    args['form'] = KlientsForm

    args['active_tab_3'] = True
    return render_to_response ( 'kli_edit_client.html', args )
