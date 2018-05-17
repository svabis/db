# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect

from database.args import create_args

from django.core.context_processors import csrf

# Abonementi
from clients.models import Klienti

# Skapji history
from lockers.models import Skapji_history

# Abonementi
from subscriptions.models import AbonementType

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
# !!!!! Client XLS eksports !!!!!
def clients_export(request):
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
        all_dates = request.POST.get('cli_no_date')
        if all_dates == "on":
            all_dates = True
        else:
            all_dates = False

        active = request.POST.get('cli_active')
        if active == "on":
            active = True
        else:
            active = False

        start_str = request.POST.get('cli_start', '')
        end_str = request.POST.get('cli_end', '')

       # Date range no picker
        if all_dates == False:
           # convert dates from string to datetime
            date_error = False
            try:
                start_date = datetime.strptime( start_str, '%Y-%m-%d').replace(tzinfo=tz)
            except:
                args['cli_start_error'] = True
                date_error = True
            try:
                end_date = datetime.strptime( end_str, '%Y-%m-%d').replace(tzinfo=tz)
            except:
                if end_str != "":
                    args['cli_end_error'] = True
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

       # Viss periods
        else:
            date_min = datetime(2018, 1, 1, 0, 0, 0, 0).replace(tzinfo=tz)
            date_max = datetime.combine( datetime.now(), time.max).replace(tzinfo=tz)

       # BS Report log
        if all_dates:
            if active == True:
                new_report = Reports( event='Active Client Report', user=args['username'] )
            else:
                new_report = Reports( event='Full Client Report', user=args['username'] )
        else:
            if active == True:
                new_report = Reports( event='Active Client Report', event_data=start_str + ' ' + end_str, user=args['username'] )
            else:
                new_report = Reports( event='Client Report', event_data=start_str + ' ' + end_str, user=args['username'] )
        new_report.save()

       # Active/All
        if active == True:
            data = []
            data_sk = []
            for k in Klienti.objects.all():
                k_sk = Skapji_history.objects.filter( client = k, checkin_time__range=[date_min, date_max] )
                if k_sk.count() > 0:
                    data.append( k )
                    data_sk.append( k_sk.count() )
        else:
            data = Klienti.objects.all()


        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="clients.xls"'

        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Klienti')

       # Sheet header, first row
        row_num = 0

        font_style = xlwt.XFStyle()
        font_style.font.bold = True

        columns = ['Klienta ID', 'Reģistrācijas Datums', 'Vārds', 'Uzvārds', 'Dzimums', 'Dzimšanas datums',
                   'Tālrunis', 'E-pasts', 'Klienta kartes Nr', 'Status', 'Biedrība',
                   'Skolnieks/Students', 'Apliecība derīga līdz', 'Invalīds', 'Apliecība derīga līdz', 'Pensionārs', 'Piezīmes']

        if active == True:
            columns.append('Apmeklējumu skaits')

        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)

       # Sheet body, remaining rows
        font_style = xlwt.XFStyle()

       # Export Data
        for row in data:
            row_num += 1
            ws.write(row_num, 0, row.id, font_style)
            try:
                ws.write(row_num, 1, row.reg_date.strftime("%Y-%m-%d"), font_style)
            except:
                pass
            ws.write(row_num, 2, row.name, font_style)
            ws.write(row_num, 3, row.surname, font_style)
            ws.write(row_num, 4, row.gender, font_style)
            try:
                ws.write(row_num, 5, row.birthday.strftime("%Y-%m-%d"), font_style)
            except:
                pass

            ws.write(row_num, 6, row.phone, font_style)
            ws.write(row_num, 7, row.e_mail, font_style)
            ws.write(row_num, 8, row.card_nr, font_style)
            ws.write(row_num, 9, row.status.status_name, font_style)
            if row.society == True:
                ws.write(row_num, 10, 'Jā', font_style)

            if row.student == True:
                ws.write(row_num, 11, 'Jā', font_style)
            try:
                ws.write(row_num, 12, row.student_until.strftime("%Y-%m-%d"), font_style)
            except:
                pass
            if row.disabled == True:
                ws.write(row_num, 13, 'Jā', font_style)
            try:
                ws.write(row_num, 14, row.disabled_until.strftime("%Y-%m-%d"), font_style)
            except:
                pass
            if row.elderly == True:
                ws.write(row_num, 15, 'JĀ', font_style)
            ws.write(row_num, 16, row.notes, font_style)

            if active == True:
                ws.write(row_num, 17, data_sk[row_num-1], font_style)

        wb.save(response)
        return response

    return render_to_response ( 'reports_main.html', args )
