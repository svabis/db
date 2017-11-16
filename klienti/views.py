# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect

from django.contrib import auth # autorisation library
from django.contrib.auth.models import User, Group

from django.core.context_processors import csrf


def new_client(request):
    args = {}
    args['help'] = False
    args['django'] = True

    args['active_tab_2'] = True
    return render_to_response ( 'kli_new_client.html', args )
