# -*- coding: utf-8 -*-
#import os       # for work with filesystem
#import re       # for regular expresions (regex)
#import datetime # for file create field
#import pytz	# to set timezone

# Klienti
from clients.models import Klienti

# Tools
from database.tools import ActiveSubscription, SubscriptionEnd

# progress bar
from tqdm import tqdm


# IMPORT DJANGO STUFF
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    def handle(self, *args, **options):

       client = Klienti.objects.all()

       for c in tqdm( range(client.count()) ):
           SubscriptionEnd( client[c] )
