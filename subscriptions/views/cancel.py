# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect

from database.args import create_args

from setup.models import Settings

from subscriptions.models import Abonementi


#============================================================
# !!!!! AB CANCEL !!!!!
def ab_cancel(request, ab_id, pageid = 1, back = 0):
    args = create_args(request)
    if args['access'] == False:
        return redirect (Settings.objects.get( key = "access denied redirect" ).value)
    if args['loged_in'] == False:
        return redirect("/login/")
    if args['admin'] != True:
        return redirect("/login/")

    try:
        ab = Abonementi.objects.get( id=int(ab_id) )
        ab.delete()
    except:
        pass

    try:
        return redirect ( 'subscr_hist', back=back, pageid=pageid )
    except:
        return redirect ( 'subscr_hist', back=back )
