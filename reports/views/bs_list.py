# -*- coding: utf-8 -*-
from database.args import create_args

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


#============================================================
# !!!!! BS XLS eksports !!!!!
def bs_export(request):
    args = create_args(request)
    if args['access'] == False:
        return redirect (Settings.objects.get( key = "access denied redirect" ).value)
    if args['loged_in'] == False:
        return redirect("/login/")
    if args['admin'] != True:
        return redirect("/login/")

    args['active_tab_5'] = True

   # BS Report log
    new_report = Reports( event='BS Report', user=args['username'] )
    new_report.save()

    bs = AbonementType.objects.get( title = "Brīvais Special" )
    bs_list = Abonementi.objects.filter( subscr = bs )

    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="BS_list.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('BS')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Abonementa ID', 'Klienta ID', 'Vārds', 'Uzvārds', 'Iegādes datums', 'Piezīmes']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

   # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

   # Export Data
    for row in bs_list:
        row_num += 1
        ws.write(row_num, 0, row.id, font_style)
        ws.write(row_num, 1, row.client.id, font_style)
        ws.write(row_num, 2, row.client.name, font_style)
        ws.write(row_num, 3, row.client.surname, font_style)
        ws.write(row_num, 4, row.purchase_date.strftime("%Y-%m-%d %H:%M"), font_style)
        ws.write(row_num, 5, row.client.notes, font_style)

    wb.save(response)
    return response
