# -*- coding: utf-8 -*-
import os       # for work with filesystem
import re       # for regular expresions (regex)

from clients.models import Klienti

import datetime
from tqdm import tqdm

# IMPORT DJANGO STUFF
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    def handle(self, *args, **options):

       print datetime.datetime.now()

       db = '/home/svabis/Tabulas/T01402GerateZoo'

       lines = [line.rstrip('\n') for line in open(db)]

# 6 s3.id
# 7 kartiņa

       for i in tqdm( range(len(lines)) ):
#       for line in lines:
#           l = line.split('\t')
           l = lines[i].split('\t')

           id = l[6]
           card = l[7].split('=')[-1]

           try:
               klient = Klienti.objects.get(s3_nr=id)
               klient.card_nr = card
               klient.save()
           except:
               print l

       print datetime.datetime.now()
