# -*- coding: utf-8 -*-
#import os       # for work with filesystem
#import re       # for regular expresions (regex)
#import datetime # for file create field
#import pytz	# to set timezone

from clients.models import * #Klienti, StatusType

# progress bar
from tqdm import tqdm

#from django.core.files import File	# for file opening

# IMPORT DJANGO STUFF
from django.core.management.base import BaseCommand, CommandError

#d = datetime.datetime( 1899, 12, 30, 0, 0 ).date()

class Command(BaseCommand):
    def handle(self, *args, **options):
#       db = '/home/svabis/Tabulas/T00801Person'
#       img_folder = '/home/svabis/Personen/'
#       lines = [line.rstrip('\n') for line in open(db)]

       counter = 0
       klienti = []

       k = Klienti.objects.all()

       biedrs = Statusi.objects.get( status_name = "Biedrs" )

       for i in tqdm( range( k.count() ) ):
           kli = k[i]
           if kli.status != biedrs:
               klienti.append( [kli, kli.status, kli.society] )
               counter += 1

       print counter

       for k in klienti:
           print k
