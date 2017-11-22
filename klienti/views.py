# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect

from django.core.context_processors import csrf

from django.db.models import Q # search in multiple columns

from klienti.forms import KlientsForm
from klienti.models import Klienti

from setup.models import Settings

from database.args import create_args

from klienti.paginator import Paginator  # import paginator
import math # for rounding up Page Counter


# !!!!! Redirect UP !!!!!
def main(request):
    return redirect('/')


# !!!!! NEW CLIENT !!!!!
def new_client(request):
    args = create_args(request)
    if args['access'] == False:
        return redirect ("http://kuvalda.lv/")

    args.update(csrf(request)) # ADD CSRF TOKEN

   # Created form POST
    if request.POST:
        form = KlientsForm( request.POST, request.FILES )

        if form.is_valid():
           # INSERT SOME STUFF HERE :D
            new_client = form.save()
            response = redirect("/client/new/")
            response.set_cookie( key='active_client', value=new_client.id )
            return response
        else:
            args['form'] = form
            return render_to_response ( 'kli_new_client.html', args )

    args['form'] = KlientsForm

    args['active_tab_2'] = True
    return render_to_response ( 'kli_new_client.html', args )

#------------------------------------------------------------------
# !!!!! EDIT CLIENT !!!!!
def edit_client(request):
    args = create_args(request)
    if args['access'] == False:
        return redirect ("http://kuvalda.lv/")

    args.update(csrf(request)) # ADD CSRF TOKEN

   # Edited form POST
    if request.POST:
        c_id = int(request.COOKIES.get(str('active_client')))
        client = Klienti.objects.get( id = c_id  )
        form = KlientsForm( request.POST, request.FILES, instance = client )

        if form.is_valid():
           # INSERT SOME STUFF HERE :D
            form.save()
            return redirect("/client/edit/")
        else:
            args['form'] = form
            return render_to_response ( 'kli_edit_client.html', args )

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
           # COMMENT
            return redirect ("/")
    else:
        return redirect ("/")

    return render_to_response ( 'kli_edit_client.html', args )


#============================================================
# !!!!! Klientu Meklēšana !!!!!
def search(request, pageid = 1):
    args = create_args(request)
    if args['access'] == False:
        return redirect ("http://kuvalda.lv/")

    args.update(csrf(request)) # ADD CSRF TOKEN

    args['active_tab_1'] = True

    results_per_page = int(Settings.objects.get( key = "search results on page" ).value)
    search_order = Settings.objects.get( key = "search results order" ).value

   # Search from POST
    if request.POST:
        post = True # Triger search from POST
        to_find = request.POST.get('search', '')

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

    response = render_to_response ( 'kli_search.html', args )
    response.set_cookie( key='search_client', value = to_find )

    return response





# !!!!! Klientu Meklēšanas response uz Main !!!!!
def search_response(request, c_id):
    args = create_args(request)
    if args['access'] == False:
        return redirect ("http://kuvalda.lv/")

    client = Klienti.objects.get( id = c_id )

    response = redirect ("/")
    response.set_cookie( key='active_client', value=client.id )
    return response

