# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect

from database.args import create_args

from django.core.context_processors import csrf

# Abonementi
from subscriptions.models import AbonementType, Abonementi

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
# !!!!! AB XLS eksports !!!!!
def ab_export(request):
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
        ab_id = request.POST.get('ab_type', '')
        ab = AbonementType.objects.get( id=ab_id )

        all_dates = request.POST.get('ab_no_date')
        if all_dates == "on":
            all_dates = True
        else:
            all_dates = False

        active = request.POST.get('ab_active')
        if active == "on":
            active = True
        else:
            active = False

        start_str = request.POST.get('ab_start', '')
        end_str = request.POST.get('ab_end', '')

       # Date range no picker
        if all_dates == False:
           # convert dates from string to datetime
            date_error = False
            try:
                start_date = datetime.strptime( start_str, '%Y-%m-%d').replace(tzinfo=tz)
            except:
                args['ab_start_error'] = True
                date_error = True
            try:
                end_date = datetime.strptime( end_str, '%Y-%m-%d').replace(tzinfo=tz)
            except:
                if end_str != "":
                    args['ab_end_error'] = True
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

       # Active/All
        if active == True:
            sales_data = Abonementi.objects.filter( subscr=ab, purchase_date__range=[date_min, date_max], ended=False ).order_by('purchase_date')
        else:
            sales_data = Abonementi.objects.filter( subscr=ab, purchase_date__range=[date_min, date_max] ).order_by('purchase_date')

       # BS Report log
        if all_dates:
            new_report = Reports( event='AB', event_data=ab.title, user=args['username'] )
        else:
            new_report = Reports( event='AB', event_data=ab.title + ' | ' + start_str + ' ' + end_str, user=args['username'] )
        new_report.save()

        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="ab.xls"' # DATUMS PIE NOSAUKUMA

        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('AB Atskaite')

       # Sheet header, first row
        row_num = 0

        font_style = xlwt.XFStyle()
        font_style.font.bold = True

        columns = ['Pārdošanas laiks', 'Aktivizēt līdz', 'Derīgs līdz', 'Atlikušo reižu skaits',
                   'Klienta ID', 'Vārds', 'Uzvārds', 'Abonements',
                   'Abonements izlietots', 'Piezīmes']
#                   'Skaits', 'Pilnā cena', 'Cena ar atlaidi', 'Apmaksa no depozīta', 'Dāvanu karte',
#                   'Apmaksā apdrošināšana', 'Apdrošinātājs', 'Pārskaitījums', 'Gala summa']

        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)

       # Sheet body, remaining rows
        font_style = xlwt.XFStyle()

       # Export Data
        for row in sales_data:
            row_num += 1

            new_time = row.purchase_date + timedelta( hours=dst( row.purchase_date ) )
            ws.write(row_num, 0, new_time.strftime("%Y-%m-%d %H:%M"), font_style)

            try:
                new_time = row.activate_before + timedelta( hours=dst( row.activate_before ) )
                ws.write(row_num, 1, new_time.strftime("%Y-%m-%d %H:%M"), font_style)
            except:
                pass

            try:
                new_time = row.best_before + timedelta( hours=dst( row.best_before ) )
                ws.write(row_num, 2, new_time.strftime("%Y-%m-%d %H:%M"), font_style)
            except:
                pass

            try:
                ws.write(row_num, 3, row.times_count, font_style)
            except:
                pass

            ws.write(row_num, 4, row.client.id, font_style)
            ws.write(row_num, 5, row.client.name, font_style)
            ws.write(row_num, 6, row.client.surname, font_style)
            ws.write(row_num, 7, row.subscr.title, font_style)

            if row.ended != False:
                ws.write(row_num, 8, 'Izlietots', font_style)

            ws.write(row_num, 9, row.client.notes, font_style)

        wb.save(response)
        return response

    return render_to_response ( 'reports_main.html', args )
