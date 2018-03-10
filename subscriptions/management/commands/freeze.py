# -*- coding: utf-8 -*-
from datetime import date

# Klienti
from clients.models import Klienti

# Abonementu iesaldes
from subscriptions.models import Abonementu_Iesalde

# progress bar
#from tqdm import tqdm


# IMPORT DJANGO STUFF
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    def handle(self, *args, **options):

       clients = Klienti.objects.all()
       counter = 0

       for c in clients:
           changes = False

           if isinstance( c.frozen_from, date ) == True:
               if c.frozen_from <= date.today():
                   c.frozen = True
                   changes = True

           if isinstance( c.frozen_until, date ) == True:
               if c.frozen_until < date.today():
                   c.frozen = False
                   c.frozen_from = None
                   c.frozen_until = None
                   changes = True

                  # delete iesaldes
                   frozen_s = Abonementu_Iesalde.objects.filter( client = c )
                   for f in frozen_s:
                       f.delete()

           if changes == True:
               print c
               c.save()
               counter += 1

       print counter


