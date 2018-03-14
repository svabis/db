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
       freeze_cancel = 0
       counter = 0

       for c in clients:
           if c.frozen:
               print c

