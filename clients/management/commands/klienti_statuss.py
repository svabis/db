# -*- coding: utf-8 -*-
import os       # for work with filesystem
import re       # for regular expresions (regex)
import datetime # for file create field
import pytz	# to set timezone

from clients.models import Klienti, StatusType

#from slugify import slugify

# IMPORT DJANGO STUFF
from django.core.files import File	# for file opening

from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    def handle(self, *args, **options):
# 0 Person no
# 4 reģ date
# 5 First name
# 6 Surname
# 8 Date of birth

# 14 Mobile 16
# 15 E-mail 17
# 25 Gender
# 31 Status
#       temp_status = StatusType.objects.all()[0]

       db = '/home/svabis/Tabulas/T00801Person'
       st = '/home/svabis/Tabulas/T00802Status'

      # read Status
       lines = [line.rstrip('\n') for line in open(st)]
       status = []
       for line in lines:
         l = line.split('\t')
         status.append( [l[0], l[5]] )

      # read Klienti
       lines = [line.rstrip('\n') for line in open(db)]
       klienti = []
       for line in lines:
         l = line.split('\t')
         klienti.append( [l[0], l[31]] )

      # print status
       for s in status:
           print s

      # print klienti
#       for k in klienti:
#           print k

      # nummurs
       print [i for i, x in enumerate(status) if x[0] == "1-23"][0]
      # vertiba
       print status[ [i for i, x in enumerate(status) if x[0] == "1-23"][0] ] [1]

       counter = 0
       kli = Klienti.objects.all()

       for k in kli:
           try:
              # klienta status no masiva
               kli_stat = klienti[[i for i, x in enumerate(status) if x[0] == k.s3_nr ][0]][1]
              # atbilstiba no status tabulas
               stat = StatusType.objects.get( status_name = status[[i for i, x in enumerate(status) if x[0] == kli_stat][0]][1] )
               k.status = stat
               k.save()
               counter += 1
               print k.name + " " + k.surname + "\t" + stat.status_name
#               print k.s3_nr
#               print stat
#               print
           except:
               pass

#       print counter
