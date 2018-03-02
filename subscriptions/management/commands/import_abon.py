# -*- coding: utf-8 -*-
import os       # for work with filesystem
import re       # for regular expresions (regex)
import datetime # for file create field
import pytz	# to set timezone

from subscriptions.models import *

import datetime

# progress bar
from tqdm import tqdm

from django.core.files import File	# for file opening

# IMPORT DJANGO STUFF
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    def handle(self, *args, **options):

#       limit = TimelimitType.objects.all()
#       for l in limit:
#           print l.id
#           print l

       db = '/home/svabis/Tabulas/abonementi'
       lines = [line.rstrip('\n') for line in open(db)]

# 0 title
# 1 short_title
# 2 cena - " Eur"

# 3 times_count <-- if tad times = True

# 4 best_before
# 5 time_limit_type <-- if tad time_limit = True

# 6 first_time 1 --> True
# 7 special 1 --> True

# 8 s3_id

# available = True

       for i in tqdm( range(len(lines)) ):
           l = lines[i].split('\t')

           times = False
           time_limit = False
           first_time = False
           special = False

           title = l[0]
           short_title = l[1]
           price = l[2].split(" ")[0]

           new_abon = AbonementType( title = l[0], short_title = l[1], price = int(l[2].split(" ")[0]) )

           if l[3] != "":
               new_abon.times = True
               new_abon.times_count = int(l[3])

           if l[4] != "":
               new_abon.best_before = int(l[4])

           try:
             if l[5] != "":
               new_abon.time_limit = True
               new_abon.time_limit_type = TimelimitType.objects.get( id = l[3] )
           except:
               new_abon.time_limit = True

           if l[6] != "":
               new_abon.first_time = True

           if l[7] != "":
               new_abon.special = True

           new_abon.s3_nr = l[8]
           new_abon.save()
