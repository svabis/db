# -*- coding: utf-8 -*-
import os       # for work with filesystem
import re       # for regular expresions (regex)
import datetime # for file create field
import pytz	# to set timezone

from clients.models import Klienti, Statusi

from slugify import slugify
import datetime

from tqdm import tqdm

# IMPORT DJANGO STUFF
from django.core.files import File	# for file opening

from django.core.management.base import BaseCommand, CommandError

d = datetime.datetime( 1899, 12, 30, 0, 0 ).date()

class Command(BaseCommand):
    def handle(self, *args, **options):

       print datetime.datetime.now()

       db = '/home/svabis/Tabulas/T00801Person'
#       img_folder = '/home/svabis/Personen0/'
       img_folder = '/home/svabis/Personen/'
       tz = pytz.timezone('UTC')
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
       gender_error = []

       temp_status = Statusi.objects.all()[0]

       for i in tqdm( range(len(lines)) ):
           l = lines[i].split('\t')

           gender_temp = ""
           if l[25] == "m":
               gender_temp = "V"
           if l[25] == "w":
               gender_temp = "S"

          # gender error
           if gender_temp == "":
               gender_error.append(l[0])
#               print "gender error\t" + str(l[0])
               error += 1

          # Phone numbers
           phone_temp = ""
           if l[13] != "":
                phone_temp += l[13] + ","
           if l[14] != "":
                phone_temp += l[14] + ","
           if l[15] != "":
                phone_temp += l[15]

          # Test Cases
           if len( phone_temp ) > 25:
                print "phone simbol count > 25\t" + str(l[0])
                error += 1
           if len( phone_temp.split('@') ) > 1:
                print "phone has @\t" + str(l[0])
                error += 1

           counter += 1

       print "gender error:"
       print gender_error
       print len(gender_error)
       print

       print str(error) + "/" + str(counter)
       print datetime.datetime.now()
