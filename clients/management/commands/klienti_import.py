# -*- coding: utf-8 -*-
import os       # for work with filesystem
import re       # for regular expresions (regex)
import datetime # for file create field
import pytz	# to set timezone

from clients.models import Klienti, StatusType

from slugify import slugify
import datetime

# IMPORT DJANGO STUFF
from django.core.files import File	# for file opening

from django.core.management.base import BaseCommand, CommandError

d = datetime.datetime( 1899, 12, 30, 0, 0 ).date()

class Command(BaseCommand):
    def handle(self, *args, **options):
       db = '/home/svabis/Tabulas/T00801Person.xls'
#       img_folder = '/home/svabis/Personen0/'
       img_folder = '/home/svabis/Personen/'
       tz = pytz.timezone('UTC')
       lines = [line.rstrip('\n') for line in open(db)]

# 0 Person no
# 4 reģ date
# 5 First name
# 6 Surname
# 8 Date of birth

# 14 Mobile 16
# 15 E-mail 17
# 25 Gender
# 7 Status

       start = False
  #     start = True
       counter = 0

       temp_status = StatusType.objects.all()[0]

       for line in lines:
         l = line.split('\t')
         if l[0] == "1-20577":
          start = True

         if start == True:
           gender_temp = ""
           if l[25] == "m":
               gender_temp = "V"
           else: # == "w":
               gender_temp = "S"

           avatar_exist = False
           birthday_exist = False

           print l[0] + "\t" + l[1]

           try:
               open_image = open( img_folder + l[0] + ".jpg", 'rb')
               avatar_temp = File( open_image  )
#               print avatar_temp
               avatar_exist = True
               new_client = ""
          # NO AVATAR
           except:
               pass

           try:
               if l[8] != '':
#                   time = d + datetime.timedelta( days = int(l[8].split('.')[0]) )
                   time = datetime.datetime.strptime( l[8], '%d/%m/%Y')
#                   print time
                   birthday_exist = True
#                   l.pop(8)

          # NO BIRTHDAY
           except:
               pass

           reg_date_temp = datetime.datetime.strptime( l[4], '%d/%m/%Y %H:%M:%S')
#           l[16] = slugify( l[16] ) # nekorekti: fizmats-inbox-lv

           if birthday_exist == True:
              # AVATAR + BIRTHDAY
               if avatar_exist == True:
                   new_client = Klienti( avatar = avatar_temp, name = l[5], surname = l[6], birthday = time, phone=l[15], e_mail=l[16],  gender = gender_temp, status=temp_status,
                                s3_nr=l[0], reg_date=reg_date_temp )
                   new_client.save()
              # BIRTHDAY
               else:
                   new_client = Klienti( name = l[5], surname = l[6], birthday = time, phone=l[15], e_mail=l[16],  gender = gender_temp, status=temp_status, s3_nr=l[0], reg_date=reg_date_temp )
                   new_client.save()
           else:
              # AVATAR
               if avatar_exist == True:
                   new_client = Klienti( avatar = avatar_temp, name = l[5], surname = l[5], phone=l[13], e_mail=l[16],  gender = gender_temp, status=temp_status, s3_nr=l[0], reg_date=reg_date_temp )
                   new_client.save()
              # NO BIRTHDAY + NO AVATAR
               else:
                   new_client = Klienti( name = l[5], surname = l[6], phone=l[15], e_mail=l[16],  gender = gender_temp, status=temp_status, s3_nr=l[0], reg_date=reg_date_temp )
                   new_client.save()

           if new_client == "":
                print l

#           print new_client
         counter += 1


       print counter
