# -*- coding: utf-8 -*-
import os       # for work with filesystem
import re       # for regular expresions (regex)
import datetime # for file create field
import pytz	# to set timezone

from clients.models import Klienti, StatusType

import datetime

# progress bar
from tqdm import tqdm

#from slugify import slugify

# IMPORT DJANGO STUFF
from django.core.files import File	# for file opening

from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    def handle(self, *args, **options):

# 0 Person no
# 31 Status

#       db = '/home/svabis/Tabulas/T00801Person'
       st = '/home/svabis/Tabulas/T00808Memo'

       print datetime.datetime.now()
#       memo = []

       lines = [line.rstrip('\n') for line in open(st)]
       print len(lines)

#       for line in lines:
       for i in tqdm( range( len(lines) ) ):
         l = lines[i].split('\t')
#         l = line.split('\t')
         temp = l[8].rstrip('\\x0d\\x0a')
         temp = temp.replace('\\x0d\\x0a', '\n')

         counter = 0

         try:
             k = Klienti.objects.get( s3_nr = l[5] )
             k.notes = temp
             k.save()
             counter += 1
         except:
             print l
#             memo.append( l )
#             pass

#       for m in memo:
#           print m

       print datetime.datetime.now()
