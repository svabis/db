# -*- coding: utf-8 -*-
import os       # for work with filesystem
import re       # for regular expresions (regex)
import datetime # for file create field
import pytz	# to set timezone

#from nodarb.models import *
from klienti.models import Klienti
#from grafiks.models import Grafiks
#from pieraksts.models import *

from slugify import slugify

# IMPORT DJANGO STUFF
from django.core.files import File	# for file opening

from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    def handle(self, *args, **options):
       db = '/home/svabis/import'
       tz = pytz.timezone('UTC')
       lines = [line.rstrip('\n') for line in open(db)]

# 0 Person no
# 1 First name
# 2 Surname
# 3 Date of birth
# 4 Mobile
# 5 E-mail
# 6 Gender
# 7 Status

#       l = lines[0].split('\t')
#       print l


       for line in lines:
#       if True:
#           line = lines[2]
           l = line.split('\t')

#           print l

           if l[6] == "m":
               gender = "V"
           else:
               gender = "S"

           email = slugify( l[5] )

#           if True:
           try:
               time = datetime.datetime.strptime( l[3], '%d/%m/%Y')
               new_client = Klienti( name = l[1], surname = l[2], birthday = time, phone=l[4], e_mail=l[5],  sex = gender )
               new_client.save()
               print new_client
           except:
               pass

