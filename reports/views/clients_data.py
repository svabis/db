# -*- coding: utf-8 -*-
from database.args import create_args

# Abonementi
from clients.models import Klienti

# Reports
from loginsys.models import Reports

# Setingi
from setup.models import Settings

# export
from django.http import HttpResponse
# XLS
import xlwt

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

   # BS Report log
    new_report = Reports( event='Full Client Report', user=args['username'] )
    new_report.save()

    data = Klienti.objects.all()

    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="BS_list.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('BS')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Klienta ID', 'Reģistrācijas Datums', 'Vārds', 'Uzvārds', 'Dzimums', 'Dzimšanas datums',
               'Tālrunis', 'E-pasts', 'Klienta kartes Nr', 'Status', 'Biedrība',
               'Skolnieks/Students', 'Apliecība derīga līdz', 'Invalīds', 'Apliecība derīga līdz', 'Pensionārs', 'Piezīmes']

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

    wb.save(response)
    return response
