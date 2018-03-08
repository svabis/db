# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect

from clients.models import Klienti, Deposit

from setup.models import Settings

from database.args import create_args


#==================================================================
# !!!!! Deposit Add !!!!!
def add_deposit(request):
    args = create_args(request)
    if args['access'] == False:
        return redirect (Settings.objects.get( key = "access denied redirect" ).value)

   # Get Active client from COOKIE
    if "active_client" in request.COOKIES:
        try:
            c_id = int(request.COOKIES.get(str('active_client')))
            client = Klienti.objects.get( id = c_id )
            if request.POST:
                amount = float( request.POST.get('deposit_add', '').split(" ")[1] )
                reason = request.POST.get('deposit_reason', '')

                try:
                    last_amount = float( Deposit.objects.filter( d_client = client).order_by('-d_date')[0].d_remain )
                except:
                    last_amount = float(0)

                temp = Deposit( d_user = args['username'], d_client = client, d_reason = reason, d_added = amount, d_remain = last_amount + amount )
                temp.save()
        except:
            pass
    return redirect("/client/edit/")
