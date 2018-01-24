# -*- coding: utf-8 -*-
import os       # for work with filesystem
import re       # for regular expresions (regex)

from clients.models import Klienti

# IMPORT DJANGO STUFF
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    def handle(self, *args, **options):
       db = '/home/svabis/T01402GeraeteZo.xls'

       lines = [line.rstrip('\n') for line in open(db)]

# 6 s3.id
# 7 Status

       for line in lines:
           l = line.split('\t')

           id = l[6]
           card = l[7].split('=')[-1]

           try:
               klient = Klienti.objects.get(s3_nr=id)
               klient.card_nr = card
               klient.save()
           except:
               print l # id + "\t" +card
