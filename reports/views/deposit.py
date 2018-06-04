# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect

from database.args import create_args

from django.core.context_processors import csrf

# Abonementi
from subscriptions.models import AbonementType

# Depozits
from clients.models import Deposit

# Reports
from loginsys.models import Reports

# Setingi
from setup.models import Settings

# export
from django.http import HttpResponse
# XLS
import xlwt

from time_corection import dst
from datetime import timedelta, datetime, date, time

import pytz
#tz = pytz.timezone('UTC')
tz = pytz.timezone('EET')

#============================================================
# !!!!! deposit eksports !!!!!
def deposit_export(request):
    args = create_args(request)
    if args['access'] == False:
        return redirect (Settings.objects.get( key = "access denied redirect" ).value)
    if args['loged_in'] == False:
        return redirect("/login/")
    if args['admin'] != True:
        return redirect("/login/")

    args['active_tab_5'] = True
    args['ab'] = AbonementType.objects.filter( available=True ).order_by('title')
    args['today'] = datetime.now()

    args.update(csrf(request)) # ADD CSRF TOKEN

    if request.POST:
       # BS Report log
        new_report = Reports( event='Deposit Report', user=args['username'] )
        new_report.save()

        deposit_raw_data = Deposit.objects.all().order_by("-d_date")

        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="deposit.xls"' # DATUMS PIE NOSAUKUMA

        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Depozīta atlikumi')

       # Sheet header, first row
        row_num = 0

        font_style = xlwt.XFStyle()
        font_style.font.bold = True

        columns = ['Atlikuma laiks', 'Klienta ID', 'Vārds', 'Uzvārds', 'Summa']

        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)

       # Sheet body, remaining rows
        font_style = xlwt.XFStyle()

        cli = []

       # Export Data
        for row in deposit_raw_data:
            if row.d_client.id not in cli:
                cli.append( row.d_client.id )
                row_num += 1

                new_time = row.d_date + timedelta( hours=dst( row.d_date ) )
                ws.write(row_num, 0, new_time.strftime("%Y-%m-%d %H:%M"), font_style)

                ws.write(row_num, 1, row.d_client.id, font_style)
                ws.write(row_num, 2, row.d_client.name, font_style)
                ws.write(row_num, 3, row.d_client.surname, font_style)

                ws.write(row_num, 4, row.d_remain, font_style)

        wb.save(response)
        return response

    return render_to_response ( 'reports_main.html', args )

