# -*- coding: utf-8 -*-
import os       # for work with filesystem
import re       # for regular expresions (regex)
import datetime # for file create field
import pytz	# to set timezone

from clients.models import * #Klienti, StatusType

import datetime

# progress bar
from tqdm import tqdm

from django.core.files import File	# for file opening

# IMPORT DJANGO STUFF
from django.core.management.base import BaseCommand, CommandError

d = datetime.datetime( 1899, 12, 30, 0, 0 ).date()

class Command(BaseCommand):
    def handle(self, *args, **options):
       db = '/home/svabis/Tabulas/T00801Person'
#       img_folder = '/home/svabis/Personen/'
       lines = [line.rstrip('\n') for line in open(db)]

# 0 Person no
# 4 reg date
# 5 First name
# 6 Surname
# 8 Date of birth

# 13 14 15 Mobile
# 16 E-mail 17
# 25 Gender
# 31 Status

       counter = 0
       error = 0
       klient_error = []
       surname_error = []
       name_error = []

       temp_status = Statusi.objects.all()[0]

       for i in tqdm( range(len(lines)) ):
           l = lines[i].split('\t')

          # Klients
           try:
               k = Klienti.objects.get( s3_nr = l[0] )
               k.name = l[5]
               k.surname = l[6]
               k.save()
#               if str(k.name) != l[5]:
#                   name_error.append(  l[0] )
#               if str(k.surname) != l[6]:
#                   surname_error.append( l[0] )
           except:
               klient_error.append( l[0] )

           counter += 1

       print "counter:\t" + str( counter )
       print "klient_error:\t" + str( len(klient_error) )
       print klient_error
       print "uzvardu_error:\t" + str( len(surname_error) )
       print surname_error
       print "vardu_error:\t" + str( len(name_error) )
       print name_error
