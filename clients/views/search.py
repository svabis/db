# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect

from django.core.context_processors import csrf

from django.db.models import Q # search in multiple columns

#from clients.forms import KlientsForm
from clients.models import Klienti
#, Blacklist

from setup.models import Settings

from database.args import create_args

from database.paginator import Paginator  # import paginator
import math # for rounding up Page Counter


#============================================================
# !!!!! Klientu Meklēšana !!!!!
def search(request, pageid = 1):
    args = create_args(request)
    if args['access'] == False:
        return redirect (Settings.objects.get( key = "access denied redirect" ).value)

    if args['loged_in'] == False:
        return redirect("/login/")

    args.update(csrf(request)) # ADD CSRF TOKEN

    args['active_tab_1'] = True

    results_per_page = int(Settings.objects.get( key = "search results on page" ).value)
    search_order = Settings.objects.get( key = "search results order" ).value

   # Search from POST
    if request.POST:
        post = True # Triger search from POST
        to_find = request.POST.get('search', '')
        if len( to_find ) < 3: # IF SEARCH STRING IS LESS THAN 3 SYMBOLS --> redirect main
            return redirect ('/')

        rez_obj = Klienti.objects.filter(
           Q( name__icontains = to_find ) |
           Q( surname__icontains = to_find ) |
           Q( e_mail__icontains = to_find ) |
           Q( phone__icontains = to_find ) ).order_by( search_order )

   # Search from COOKIE
    else:
        to_find = request.COOKIES.get(str('search_client'))

        rez_obj = Klienti.objects.filter(
           Q( name__icontains = to_find ) |
           Q( surname__icontains = to_find ) |
           Q( e_mail__icontains = to_find ) |
           Q( phone__icontains = to_find ) ).order_by( search_order )

   # Paginate Search results
    if int(pageid) < 1: # negative page number --> 404
        return redirect ('/')

    pagecount = int(math.ceil( int(rez_obj.count()) / float( results_per_page ))) # integer identical to range by count

    if int(pageid) > pagecount and int(pageid) > 1: # pageid exceeds pagecount --> 404
        return redirect ('/')

    start_obj = int(pageid) * results_per_page - results_per_page # start from image NR
    end_obj = int(pageid) * results_per_page # end with image NR
    if end_obj > rez_obj.count(): # if end NR exceeds limit set it to end NR
        end_obj = rez_obj.count()

    args['search'] = to_find
    args['paginator'] = Paginator( pagecount, pageid )
    args['results'] = rez_obj.order_by('surname')[start_obj:end_obj] # -argument is for negative sort

    response = render_to_response ( 'clients_search.html', args )
    response.set_cookie( key='search_client', value = to_find )

    return response


# !!!!! Klientu Meklēšanas response uz Main !!!!!
def search_response(request, c_id):
    args = create_args(request)
    if args['access'] == False:
        return redirect (Settings.objects.get( key = "access denied redirect" ).value)

    if args['loged_in'] == False:
        return redirect("/login/")

    client = Klienti.objects.get( id = c_id )

    response = redirect ("/")
    response.set_cookie( key='active_client', value=client.id )
    return response

