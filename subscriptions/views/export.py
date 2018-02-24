# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect

from database.args import create_args

from setup.models import Settings

from subscriptions.models import *

# Klienta modelis
from clients.models import Klienti

# export
from django.http import HttpResponse
# CSV
import csv
# XLS
import xlwt
from datetime import datetime, timedelta


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
    response['Content-Disposition'] = 'attachment; filename="' + str(c_id) + '.csv"'

    writer = csv.writer(response)
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
    response['Content-Disposition'] = 'attachment; filename="' + str(c_id) + '.xls"'

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
