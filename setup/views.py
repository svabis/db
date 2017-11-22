# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect

from django.core.context_processors import csrf

from database.args import create_args

from setup.models import Settings


def settings(request):
    args = create_args(request)
    if args['access'] == False:
        return redirect ("http://kuvalda.lv/")

    args['active_tab_7'] = True

    args['settings'] = Settings.objects.all()

    return render_to_response ( 'settings.html', args )
