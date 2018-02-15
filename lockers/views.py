# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect

from django.core.context_processors import csrf

from database.args import create_args

from setup.models import Settings

from clients.models import Klienti
from lockers.models import Skapji, Skapji_history

import unicodedata # locker data unicode normalize

# export
from django.http import HttpResponse
# CSV
import csv
# XLS
import xlwt
from datetime import datetime

#============================================================
# !!!!! SKAPĪŠI !!!!!
def locker(request):
    args = create_args(request)
    if args['access'] == False:
        return redirect (Settings.objects.get( key = "access denied redirect" ).value)

    if args['loged_in'] == False:
        return redirect("/login/")

    if "active_client" in request.COOKIES:
        c_id = int(request.COOKIES.get(str('active_client')))
        client = Klienti.objects.get( id = c_id )
    else:
        redirect ("/")

   # DISABLED LOCKERS
    dml_value = Settings.objects.get( key = "disabled man locker" ).value
    dwl_value = Settings.objects.get( key = "disabled woman locker" ).value
   # convert unicode to string
    dml_value = unicodedata.normalize('NFKD', dml_value).encode('ascii','ignore')
    dwl_value = unicodedata.normalize('NFKD', dwl_value).encode('ascii','ignore')

   # split string to array
    dml = dml_value.split(",")
    dwl = dwl_value.split(",")

   # convert arrays to int
    dml = map(int, dml)
    dwl = map(int, dwl)

    args['dm'] = dml
    args['dw'] = dwl

   # LOCKER COLORS FROM SETTINGS
    args['woman_locker_color'] = Settings.objects.get( key = "woman locker color" ).value
    args['man_locker_color'] = Settings.objects.get( key = "man locker color" ).value

    lockers_filled = []
    lockers_temp = Skapji.objects.filter( locker_type = client.gender )
    for n in lockers_temp:
        lockers_filled.append( int(n.number) )

   # ADD DISABLED LOCKERS
    if client.gender == "V":
        lockers_filled = lockers_filled + dml
    else:
        lockers_filled = lockers_filled + dwl

    args['print'] = lockers_filled

    lockers = []
   # MALE LOCKERS
    if client.gender == "V":
       for i in range(1, int(Settings.objects.get( key = "man locker count" ).value) + 1 ):
           if i not in lockers_filled:
               lockers.append([i,0])
           else:
               lockers.append([i,1])

   # FEMALE LOCKERS
    else:
       for i in range(1, int(Settings.objects.get( key = "woman locker count" ).value) + 1 ):
           if i not in lockers_filled:
               lockers.append([i,0])
           else:
               lockers.append([i,1])

    args['lockers'] = lockers
    args['gender'] = client.gender
    return render_to_response ( 'locker.html', args )


#============================================================
# !!!! CHECK IN !!!!!
def locker_checkin(request, gender, locker_nr):
    if "active_client" in request.COOKIES:
        c_id = int(request.COOKIES.get(str('active_client')))
        client = Klienti.objects.get( id = c_id )

    args = create_args(request)
    if args['access'] == False:
        return redirect (Settings.objects.get( key = "access denied redirect" ).value)

    if args['loged_in'] == False:
        return redirect("/login/")

    try:
       # !!!!! Test if client is not checked in already !!!!!
        locker = Skapji.objects.get( client = client )
    except:
        try:
           # !!!!! Test if locker is available !!!!!
            locker = Skapji.objects.get( number = locker_nr )
        except:
            new_checkin = Skapji( number = locker_nr, locker_type = gender, client = client )
            new_checkin.save()

    return redirect ('/')


#============================================================
# !!!! CHECK OUT !!!!!
def locker_checkout(request):
    args = create_args(request)
    if args['access'] == False:
        return redirect (Settings.objects.get( key = "access denied redirect" ).value)

    if args['loged_in'] == False:
        return redirect("/login/")

    if "active_client" in request.COOKIES:
        c_id = int(request.COOKIES.get(str('active_client')))
        client = Klienti.objects.get( id = c_id )

    try:
        locker = Skapji.objects.get( client = client )
        new_hist = Skapji_history( number = locker.number, locker_type = locker.locker_type, client = locker.client, checkin_time = locker.checkin_time )
        new_hist.save()
        locker.delete()
    except:
        pass

    return redirect ('/')


#============================================================
# !!!!! Apmeklējumu vēsture !!!!!
def history(request):
    args = create_args(request)
    if args['access'] == False:
        return redirect (Settings.objects.get( key = "access denied redirect" ).value)

    if args['loged_in'] == False:
        return redirect("/login/")

    if "active_client" in request.COOKIES:
        c_id = int(request.COOKIES.get(str('active_client')))
        client = Klienti.objects.get( id = c_id )

    try:
        args['data'] = Skapji_history.objects.filter( client = client ).order_by('-checkin_time')
    except:
        args['no_data'] = True

    try:
        args['new_data'] = Skapji.objects.get( client = client )
    except:
        pass

    return render_to_response ( 'lockers_history.html', args )

#============================================================
# !!!!! Kas Klubā !!!!!
def persons_in_club(request):
    args = create_args(request)
    if args['access'] == False:
        return redirect (Settings.objects.get( key = "access denied redirect" ).value)

   # LOCKER COLORS FROM SETTINGS
    args['woman_locker_color'] = Settings.objects.get( key = "woman locker color" ).value
    args['man_locker_color'] = Settings.objects.get( key = "man locker color" ).value

    args['active_tab_4'] = True
    args['data'] = Skapji.objects.all().order_by( 'checkin_time' )

    return render_to_response ( 'in_club.html', args )


# !!!!! Klientu Meklēšanas pēc skapīša !!!!!
def search_by_locker(request, c_id):
    args = create_args(request)
    if args['access'] == False:
        return redirect (Settings.objects.get( key = "access denied redirect" ).value)

    if args['loged_in'] == False:
        return redirect("/login/")

    client = Klienti.objects.get( id = c_id )

    response = redirect ("/")
    response.set_cookie( key='active_client', value=client.id )
    return response



#============================================================
# !!!!!               DATU EKSPORTS CSV/XLS             !!!!!
#============================================================
# !!!!! Vēsture CSV eksports !!!!!
def history_csv(request):
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

   # THIS MOMENT
    try:
        data = Skapji.objects.get( client = client )
        writer.writerow( [str(data.number), data.checkin_time.strftime("%Y-%m-%d %H:%M")] )
    except:
        pass

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
def history_xls(request):
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

   # THIS MOMENT
    try:
        data = Skapji.objects.get( client = client )
        ws.write( 1,0, str(data.number), font_style)
        ws.write( 1,1, data.checkin_time.strftime("%Y-%m-%d %H:%M"), font_style )
        row_num += 1
    except:
        pass

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
