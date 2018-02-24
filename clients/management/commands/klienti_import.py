# -*- coding: utf-8 -*-
import os       # for work with filesystem
import re       # for regular expresions (regex)
import datetime # for file create field
import pytz	# to set timezone

from clients.models import Klienti, StatusType

import datetime

# progress bar
from tqdm import tqdm

from django.core.files import File	# for file opening

# IMPORT DJANGO STUFF
from django.core.management.base import BaseCommand, CommandError

d = datetime.datetime( 1899, 12, 30, 0, 0 ).date()

class Command(BaseCommand):
    def handle(self, *args, **options):

       print datetime.datetime.now()

       db = '/home/svabis/Tabulas/T00801Person'
       img_folder = '/home/svabis/Personen0/'
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

       start = False
       start = True
       counter = 0

       temp_status = StatusType.objects.all()[0]

       for i in tqdm( range(len(lines)) ):
         l = lines[i].split('\t')
    #     if l[0] == "1-20577":
    #      start = True

         if start == True:
           gender_temp = ""
           if l[25] == "m":
               gender_temp = "V"
           else: # == "w":
               gender_temp = "S"

           avatar_exist = False
           birthday_exist = False

          # empty client for test if client is created
           new_client = ""

#           print l[0] + "\t" + l[1]

           try:
               open_image = open( img_folder + l[0] + ".jpg", 'rb')
               avatar_temp = File( open_image  )
               avatar_exist = True
          # NO AVATAR
           except:
               pass

           try:
               if l[8] != '':
#                   time = d + datetime.timedelta( days = int(l[8].split('.')[0]) )
                   time = datetime.datetime.strptime( l[8], '%d/%m/%Y')
                   birthday_exist = True
          # NO BIRTHDAY
           except:
               pass

           reg_date_temp = datetime.datetime.strptime( l[4], '%d/%m/%Y %H:%M:%S')

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
                print l
           if len( phone_temp.split('@') ) > 1:
                print l

    # !!!!! CREATE OBJECTS !!!!!
           if birthday_exist == True:
              # AVATAR + BIRTHDAY
               if avatar_exist == True:
                   new_client = Klienti( avatar = avatar_temp, name = l[5], surname = l[6], birthday = time, phone=phone_temp, e_mail=l[16],  gender = gender_temp, status=temp_status,
                                s3_nr=l[0], reg_date=reg_date_temp )
                   new_client.save()
              # BIRTHDAY
               else:
                   new_client = Klienti( name = l[5], surname = l[6], birthday = time, phone=phone_temp, e_mail=l[16],  gender = gender_temp, status=temp_status, s3_nr=l[0], reg_date=reg_date_temp )
                   new_client.save()
           else:
              # AVATAR
               if avatar_exist == True:
                   new_client = Klienti( avatar = avatar_temp, name = l[5], surname = l[5], phone=phone_temp, e_mail=l[16],  gender = gender_temp, status=temp_status, s3_nr=l[0], reg_date=reg_date_temp )
                   new_client.save()
              # NO BIRTHDAY + NO AVATAR
               else:
                   new_client = Klienti( name = l[5], surname = l[6], phone=phone_temp, e_mail=l[16],  gender = gender_temp, status=temp_status, s3_nr=l[0], reg_date=reg_date_temp )
                   new_client.save()

          # no object was created --> print line's first column
           if new_client == "":
                print l[0]

         counter += 1

       print counter
       print datetime.datetime.now()
