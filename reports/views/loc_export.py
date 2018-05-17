# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect

from database.args import create_args

from django.core.context_processors import csrf

# Lockers
from lockers.models import Skapji_history

# Subscriptions
from subscriptions.models import AbonementType

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
tz = pytz.timezone('EET')

#============================================================
# !!!!! Apmeklejuma eksports !!!!!
def lockers_export(request):
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
        start_str = request.POST.get('loc_start', '')
        end_str = request.POST.get('loc_end', '')

       # BS Report log
        new_report = Reports( event='Lockers Report', event_data=start_str + ' ' + end_str, user=args['username'] )
        new_report.save()

       # convert dates from string to datetime
        date_error = False
        try:
            start_date = datetime.strptime( start_str, '%Y-%m-%d').replace(tzinfo=tz)
        except:
            args['loc_start_error'] = True
            date_error = True
        try:
           end_date = datetime.strptime( end_str, '%Y-%m-%d').replace(tzinfo=tz)
        except:
           if end_str != "":
               args['loc_end_error'] = True
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

        lockers_data = Skapji_history.objects.filter( checkin_time__range=[date_min, date_max] ).order_by('checkin_time')

        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="lockers.xls"' # DATUMS PIE NOSAUKUMA ?

        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Apmeklējums')

       # Sheet header, first row
        row_num = 0

        font_style = xlwt.XFStyle()
        font_style.font.bold = True

        columns = ['Ienākšanas laiks', 'Iziešanas laiks', 'Klienta ID', 'Vārds', 'Uzvārds' ]
#                   'Skaits', 'Pilnā cena', 'Cena ar atlaidi', 'No depozīta', 'Dāvanu karte',
#                   'Sedz apdrošināšana', 'Apdrošinātājs', 'Pārskaitījums', 'Gala summa']

        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)

       # Sheet body, remaining rows
        font_style = xlwt.XFStyle()

       # Export Data
        for row in lockers_data:
            row_num += 1

            new_time = row.checkin_time + timedelta( hours=dst( row.checkin_time ) )
            ws.write(row_num, 0, new_time.strftime("%Y-%m-%d %H:%M"), font_style)

            new_time = row.checkout_time + timedelta( hours=dst( row.checkout_time ) )
            ws.write(row_num, 1, new_time.strftime("%Y-%m-%d %H:%M"), font_style)

            ws.write(row_num, 2, row.client.id, font_style)
            ws.write(row_num, 3, row.client.name, font_style)
            ws.write(row_num, 4, row.client.surname, font_style)

        wb.save(response)
        return response

    return render_to_response ( 'reports_main.html', args )
