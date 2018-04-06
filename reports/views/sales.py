# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect

from database.args import create_args

from django.core.context_processors import csrf

# Abonementi
from subscriptions.models import *

# Reports
from loginsys.models import Reports

# Setingi
from setup.models import Settings

# export
from django.http import HttpResponse
# XLS
import xlwt

from datetime import timedelta, datetime, date, time

import pytz
#tz = pytz.timezone('UTC')
tz = pytz.timezone('EET')

#============================================================
# !!!!! BS XLS eksports !!!!!
def sales_export(request):
    args = create_args(request)
    if args['access'] == False:
        return redirect (Settings.objects.get( key = "access denied redirect" ).value)
    if args['loged_in'] == False:
        return redirect("/login/")
    if args['admin'] != True:
        return redirect("/login/")

    args['active_tab_5'] = True
    args['today'] = datetime.now()

    args.update(csrf(request)) # ADD CSRF TOKEN

    if request.POST:
        start_str = request.POST.get('sale_start', '')
        end_str = request.POST.get('sale_end', '')

       # BS Report log
        new_report = Reports( event='Sales Report '+ start_str + ' ' + end_str , user=args['username'] )
        new_report.save()

       # convert dates from string to datetime
        date_error = False
        try:
            start_date = datetime.strptime( start_str, '%Y-%m-%d').replace(tzinfo=tz)
        except:
            args['sale_start_error'] = True
            date_error = True
        try:
           end_date = datetime.strptime( end_str, '%Y-%m-%d').replace(tzinfo=tz)
        except:
           if end_str != "":
               args['sale_end_error'] = True
               date_error = True

       # dates error
        if date_error == True:
            return render_to_response ( 'reports_main.html', args )

       # set dates
        date_min = datetime.combine(start_date, time.min).replace(tzinfo=tz)
        try:
            date_max = datetime.combine(end_date, time.max).replace(tzinfo=tz)
        except:
            date_max = datetime.combine(start_date, time.max).replace(tzinfo=tz)

        sales_data = Abonementu_Apmaksa.objects.filter( date__range=[date_min, date_max] )

        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="sales.xls"' # DATUMS PIE NOSAUKUMA

        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Pārdotie AB')

       # Sheet header, first row
        row_num = 0

        font_style = xlwt.XFStyle()
        font_style.font.bold = True

        columns = ['Pārdošanas laiks', 'Klienta ID', 'Vārds', 'Uzvārds', 'Abonements',
                   'Skaits', 'Pilnā cena', 'Cena ar atlaidi', 'Apmaksa no depozīta', 'Dāvanu karte',
                   'Apmaksā apdrošināšana', 'Apdrošinātājs', 'Pārskaitījums', 'Gala summa']

        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)

       # Sheet body, remaining rows
        font_style = xlwt.XFStyle()

       # Export Data
        for row in sales_data:
            row_num += 1
            ws.write(row_num, 0, row.date.strftime("%Y-%m-%d %H:%M"), font_style)
            ws.write(row_num, 1, row.client.id, font_style)
            ws.write(row_num, 2, row.client.name, font_style)
            ws.write(row_num, 3, row.client.surname, font_style)
            ws.write(row_num, 4, row.subscr.subscr.title, font_style)

            ws.write(row_num, 5, row.count, font_style)
            ws.write(row_num, 6, row.full_price, font_style)
            ws.write(row_num, 7, row.discount_price, font_style)
            ws.write(row_num, 8, row.from_deposit, font_style)
            ws.write(row_num, 9, row.from_gift_card, font_style)

            ws.write(row_num, 10, row.insurance_cash, font_style)
            if row.insurance != None:
                ws.write(row_num, 11, row.insurance.title, font_style)
            if row.transfer == True:
                ws.write(row_num, 12, 'Pārskaitījums', font_style)
            ws.write(row_num, 13, row.final_price, font_style)

        wb.save(response)
        return response

    return render_to_response ( 'reports_main.html', args )
