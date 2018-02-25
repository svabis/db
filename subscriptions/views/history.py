# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect

#from django.core.context_processors import csrf

from database.args import create_args

from setup.models import Settings

# Abonementi
from subscriptions.models import *

# Klienta modelis
from clients.models import Klienti

# import paginator
from database.paginator import Paginator
import math

#from datetime import timedelta, datetime

#============================================================
# !!!!! SUBSCRIPTION HISTORY !!!!!
def subscription_history(request, pageid = 1):
    args = create_args(request)
    if args['access'] == False:
        return redirect (Settings.objects.get( key = "access denied redirect" ).value)

    if args['loged_in'] == False:
        return redirect("/login/")

    results_per_page = int(Settings.objects.get( key = "search results on page" ).value)

   # Get Active client from COOKIE
    if "active_client" in request.COOKIES:
        try:
            c_id = int(request.COOKIES.get(str('active_client')))
            cli = Klienti.objects.get( id = c_id )

            data = Abonementi.objects.filter( client = cli ).order_by('-purchase_date')

           # Paginate results
            if int(pageid) < 1: # negative page number --> 404
                return redirect ('/client/edit/')

            pagecount = int(math.ceil( int(data.count()) / float( results_per_page ))) # integer identical to range by count

            if int(pageid) > pagecount and int(pageid) > 1: # pageid exceeds pagecount --> 404
                return redirect ('/client/edit/')

            start_obj = int(pageid) * results_per_page - results_per_page # start from image NR
            end_obj = int(pageid) * results_per_page # end with image NR
            if end_obj > data.count(): # if end NR exceeds limit set it to end NR
                end_obj = data.count()

            args['paginator'] = Paginator( pagecount, pageid )
            args['data'] = data[start_obj:end_obj]

        except:
            pass
    return render_to_response ( 'subscription_history.html', args )

