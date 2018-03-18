# -*- coding: utf-8 -*-
from clients.models import *

# progress bar
from tqdm import tqdm

# IMPORT DJANGO STUFF
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    def handle(self, *args, **options):
       counter = 0
       klienti = []

       k = Klienti.objects.all()

       biedrs = Statusi.objects.get( status_name = "Biedrs" )

       for i in tqdm( range( k.count() ) ):
           kli = k[i]
           if kli.status != biedrs:
               klienti.append( [kli, kli.status, kli.society] )
               counter += 1

       for k in klienti:
           print k

       print counter
