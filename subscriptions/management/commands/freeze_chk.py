# -*- coding: utf-8 -*-
#import os       # for work with filesystem
#import re       # for regular expresions (regex)
#import datetime
from datetime import date
#import pytz	# to set timezone

# Klienti
from clients.models import Klienti

# Abonementu iesaldes
#from subscriptions.models import Abonementu_Iesalde

# Tools
#from database.tools import ActiveSubscription, SubscriptionEnd

# progress bar
from tqdm import tqdm


# IMPORT DJANGO STUFF
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    def handle(self, *args, **options):

       clients = Klienti.objects.all()

       frozen = []
       counter = 0

       for c in clients:
           changes = 0

           if c.frozen:
               frozen.append( c )

           if isinstance( c.frozen_from, date ) == True:
#               if c.frozen_from >= date.today():
                   changes = 1

           if isinstance( c.frozen_until, date ) == True:
#               if c.frozen_until < date.today():
                   changes += 1

           if changes != 0:
               print c
               print changes
               counter += 1


       print
       print "COUNTER\t" + str(counter)

       print
       print
       for f in frozen:
           print f

