# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect

from django.core.context_processors import csrf

from database.args import create_args

from setup.models import Settings

from subscriptions.models import AbonementType

# Klienta modelis
from clients.models import Klienti

# export
from django.http import HttpResponse
# CSV
import csv
# XLS
import xlwt
from datetime import datetime

#============================================================
# !!!!! ABONEMENTI !!!!!
def subscription(request, back=False):
    args = create_args(request)
    if args['access'] == False:
        return redirect (Settings.objects.get( key = "access denied redirect" ).value)

    if args['loged_in'] == False:
        return redirect("/login/")

   # return path from this view
    if back == "edit":
        args['back'] = "/client/edit/"

    else:
        args['back'] = "/"

    card_cost = int(Settings.objects.get( key = "client card price" ).value)

    args['card'] = card_cost

    args['abonementi'] = AbonementType.objects.filter( position = 1, available = True )

    args['vienreiz'] = AbonementType.objects.filter( position = 2, available = True )

    args['special'] = AbonementType.objects.filter( position = 3, available = True )

    args['first_time'] = AbonementType.objects.filter(  position = 4, available = True )

    return render_to_response ( 'subscription_choise.html', args )


#============================================================
# !!!!! ABONEMENTA APMAKSA !!!!!
def subscription_payment(request):
    args = create_args(request)
    if args['access'] == False:
        return redirect (Settings.objects.get( key = "access denied redirect" ).value)

    if args['loged_in'] == False:
        return redirect("/login/")

    return render_to_response ( 'subscription_payment.html', args )


#============================================================
# !!!!! SUBSCRIPTION HISTORY !!!!!
def subscription_history(request):
    args = create_args(request)
    if args['access'] == False:
        return redirect (Settings.objects.get( key = "access denied redirect" ).value)

    if args['loged_in'] == False:
        return redirect("/login/")

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# !!!!! INSERT BRAIN HERE !!!!!
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    return render_to_response ( 'subscription_history.html', args )


#============================================================
# !!!!! ABONEMENTA IESLADĒŠANA !!!!!
def subscription_freeze(request):
    args = create_args(request)
    if args['access'] == False:
        return redirect (Settings.objects.get( key = "access denied redirect" ).value)

    if args['loged_in'] == False:
        return redirect("/login/")

    return render_to_response ( 'subscription_freeze.html', args )


#============================================================
# !!!!!               DATU EKSPORTS CSV/XLS             !!!!!
#============================================================
# !!!!! Vēsture CSV eksports !!!!!
def subscription_history_csv(request):
    args = create_args(request)
    if args['access'] == False:
        return redirect (Settings.objects.get( key = "access denied redirect" ).value)

    if args['loged_in'] == False:
        return redirect("/login/")

    if "active_client" in request.COOKIES:
        c_id = int(request.COOKIES.get(str('active_client')))
        client = Klienti.objects.get( id = c_id )

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="history.csv"'

    writer = csv.writer(response)
    writer.writerow(['Klienta ID', str(c_id)])
    writer.writerow(['locker_nr', 'check_in_time', 'check_out_time'])

   # HISTORY
    try:
        data = Skapji_history.objects.filter( client = client ).order_by('-checkin_time') #.values_list('number', 'checkin_time', 'checkout_time')
        for d in data:
            writer.writerow( [str(d.number), d.checkin_time.strftime("%Y-%m-%d %H:%M"), d.checkout_time.strftime("%Y-%m-%d %H:%M")] )
    except:
        pass

    return response


#============================================================
# !!!!! Vēsture XLS eksports !!!!!
def subscription_history_xls(request):
    args = create_args(request)
    if args['access'] == False:
        return redirect (Settings.objects.get( key = "access denied redirect" ).value)

    if args['loged_in'] == False:
        return redirect("/login/")

    if "active_client" in request.COOKIES:
        c_id = int(request.COOKIES.get(str('active_client')))
        client = Klienti.objects.get( id = c_id )

    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="history.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Vēsture')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['locker_nr', 'check_in_time', 'check_out_time']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

   # HISTORY
    rows = Skapji_history.objects.filter( client = client ).order_by('-checkin_time').values_list('number', 'checkin_time', 'checkout_time')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            if isinstance(row[col_num], datetime):
                ws.write(row_num, col_num, row[col_num].strftime("%Y-%m-%d %H:%M"), font_style)
            else:
                ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response
