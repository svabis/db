# -*- coding: utf-8 -*-
import os       # for work with filesystem
import re       # for regular expresions (regex)
import datetime # for file create field
import pytz	# to set timezone

from klienti.models import Klienti, StatusType

from slugify import slugify

# IMPORT DJANGO STUFF
from django.core.files import File	# for file opening

from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    def handle(self, *args, **options):
       db = '/home/svabis/import'
#       img_folder = '/home/svabis/Personen0/'
       img_folder = '/home/svabis/Personen/'
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

       start = False
       start = True
       counter = 0

       temp_status = StatusType.objects.all()[0]

       for line in lines:
         l = line.split('\t')
         if l[0] == "1-20576":
          start = True

         if start == True:
           if l[6] == "m":
               gender_temp = "V"
           else:
               gender_temp = "S"

           email = slugify( l[5] )

           avatar_exist = False
           birthday_exist = False

           print l[0] + "\t" + l[1]

           try:
               open_image = open( img_folder + l[0] + ".jpg", 'rb')
               avatar_temp = File( open_image  )
#               print avatar_temp
               avatar_exist = True
          # NO AVATAR
           except:
               pass

           try:
               if l[3] != '':
                   time = datetime.datetime.strptime( l[3], '%d/%m/%Y')
#                   print time
                   birthday_exist = True
          # NO BIRTHDAY
           except:
               pass

           if birthday_exist == True:
              # AVATAR + BIRTHDAY
               if avatar_exist == True:
                   new_client = Klienti( avatar = avatar_temp, name = l[1], surname = l[2], birthday = time, phone=l[4], e_mail=l[5],  gender = gender_temp, status=temp_status, s3_nr=l[0] )
                   new_client.save()
              # BIRTHDAY
               else:
                   new_client = Klienti( name = l[1], surname = l[2], birthday = time, phone=l[4], e_mail=l[5],  gender = gender_temp, status=temp_status, s3_nr=l[0] )
                   new_client.save()
           else:
              # AVATAR
               if avatar_exist == True:
                   new_client = Klienti( avatar = avatar_temp, name = l[1], surname = l[2], phone=l[4], e_mail=l[5],  gender = gender_temp, status=temp_status, s3_nr=l[0] )
                   new_client.save()
              # NO BIRTHDAY + NO AVATAR
               else:
                   new_client = Klienti( name = l[1], surname = l[2], phone=l[4], e_mail=l[5],  gender = gender_temp, status=temp_status, s3_nr=l[0] )
                   new_client.save()

#           print new_client
         counter += 1


       print counter
