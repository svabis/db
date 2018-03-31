# -*- coding: utf-8 -*-
from subscriptions.models import *
from datetime import datetime, timedelta

# progress bar
#from tqdm import tqdm

from django.core.files import File	# for file opening

# IMPORT DJANGO STUFF
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    def handle(self, *args, **options):

       counter = 0

       start_date = datetime(2018, 3, 16, 22, 00)
       end_date = datetime(2018, 3, 29, 11, 00)

       print start_date
       print end_date

       ab = Abonementu_Apmaksa.objects.filter( date__range=[start_date, end_date])
       print ab.count()

#       for i in tqdm( range( ab.count() ) ):
#       for a in ab:
#            if a.transfer == True:
#                 a.transfer = False
#            else:
#                 a.transfer = True
#            print a.transfer
#            a.save()
