# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect

from database.args import create_args

from django.core.context_processors import csrf

# Abonementi
from subscriptions.models import *

# Setingi
from setup.models import Settings

# export
from django.http import HttpResponse
# XLS
import xlwt

from datetime import timedelta, datetime, date, time

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

       # convert dates from string to datetime
        date_error = False
        try:
            start_date = datetime.strptime( start_str, '%Y-%m-%d')
        except:
            args['sale_start_error'] = True
            date_error = True
        try:
           end_date = datetime.strptime( end_str, '%Y-%m-%d')
        except:
           if end_str != "":
               args['sale_end_error'] = True
               date_error = True

       # dates error
        if date_error == True:
            return render_to_response ( 'reports_main.html', args )

        args['sales_data'] = Abonementu_Apmaksa.objects.all()

#        response = HttpResponse(content_type='application/ms-excel')
#        response['Content-Disposition'] = 'attachment; filename="sales.xls"' # DATUMS PIE NOSAUKUMA

#        wb = xlwt.Workbook(encoding='utf-8')
#        ws = wb.add_sheet('Pārdotie AB')

       # Sheet header, first row
#        row_num = 0

#        font_style = xlwt.XFStyle()
#        font_style.font.bold = True

#        columns = ['Abonementa ID', 'Klienta ID', 'Vārds', 'Uzvārds', 'Iegādes datums', 'Piezīmes']

#        for col_num in range(len(columns)):
#            ws.write(row_num, col_num, columns[col_num], font_style)

       # Sheet body, remaining rows
#        font_style = xlwt.XFStyle()

       # Export Data
#        for row in bs_list:
#            row_num += 1
#            ws.write(row_num, 0, row.id, font_style)
#            ws.write(row_num, 1, row.client.id, font_style)
#            ws.write(row_num, 2, row.client.name, font_style)
#            ws.write(row_num, 3, row.client.surname, font_style)
#            ws.write(row_num, 4, row.purchase_date.strftime("%Y-%m-%d %H:%M"), font_style)
#            ws.write(row_num, 5, row.client.notes, font_style)

#        wb.save(response)
#        return response

    return render_to_response ( 'reports_main.html', args )
