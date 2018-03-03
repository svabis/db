# -*- coding: utf-8 -*-
import os       # for work with filesystem
import re       # for regular expresions (regex)
import datetime # for file create field
import pytz	# to set timezone

from clients.models import Klienti
from subscriptions.models import *

import datetime

# progress bar
from tqdm import tqdm

from django.core.files import File	# for file opening

# IMPORT DJANGO STUFF
from django.core.management.base import BaseCommand, CommandError

def laiks(time):
    men = time.split(".")[1]
    if len(men) < 2:
        men = "0" + men
    dat = (time.split(".")[2]).split(" ")[0]
    if len(dat) < 2:
        dat = "0" + dat
    stu = (time.split(":")[0]).split(" ")[1]
    if len(stu) < 2:
        stu = "0" + stu
    min = time.split(":")[1]
    if len(min) < 2:
        min = "0" + min
    sek = time.split(":")[2]
    if len(sek) < 2:
        sek = "0" + sek
    return time.split(".")[0] + "." + men + "." + dat + " " + stu + ":" + min + ":" + sek


class Command(BaseCommand):
    def handle(self, *args, **options):

       db = '/home/svabis/Tabulas/ZNB2.txt'
       lines = [line.rstrip('\n') for line in open(db)]
       lines = [line.rstrip('\r\n') for line in open(db)]

# 0 id << NAH
# 2 nosaukums << NAH
# 3 manipulation << NAH


# 1 .split(',')[0] <-- s3_nr Abonementu tips
# 4 s3_nr (Klients)

# 5 activation

# 6 real activation
# 7 real best_before

       save = 0
       client_error = []
       abon_error = []
       error = []

       for i in tqdm( range(len(lines)) ):
           l = lines[i].split(';')

           if True:
               try:
                   temp_client = Klienti.objects.get( s3_nr = l[4].split('"')[1] )
               except:
                   client_error.append(l[0])

               try:
                   new_abon_tips = AbonementType.objects.get( s3_nr = l[1].split(',')[0] )
               except:
                   abon_error.append(l[0])

              # Laiki
               if l[6] != "":
                   activate_date = datetime.datetime.strptime( laiks(l[6])[:19], '%Y.%m.%d %H:%M:%S')
               else:
                   activate_date = datetime.datetime.strptime( laiks(l[5])[:19], '%Y.%m.%d %H:%M:%S')

               best_before_date = activate_date + datetime.timedelta( days = 30*new_abon_tips.best_before )

              # veido abonementu
               try:
                   new_subscr = Abonementi( client=temp_client,
                                        subscr=new_abon_tips,
                                        price=new_abon_tips.price,

                                        purchase_date=activate_date,
                                        activation_date=activate_date,

                                        activate_before=best_before_date,
                                        best_before=best_before_date,

                                        times_count=new_abon_tips.times_count )
                   new_subscr.save()
                   save += 1
               except:
                   error.append(l[0])

       print
       print "save:\t" + str(save)
       print
       print "klientu error:\t" + str( len(client_error) )
       print client_error
       print
       print "abon error:\t" + str( len(abon_error) )
       print abon_error
       print
       print "error:\t" + str( len(error) )
