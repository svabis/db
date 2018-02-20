# -*- coding: utf-8 -*-
import os       # for work with filesystem
import re       # for regular expresions (regex)

from clients.models import Klienti

# IMPORT DJANGO STUFF
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    def handle(self, *args, **options):
#       db = '/home/svabis/T01402GeraeteZo.xls'

#       lines = [line.rstrip('\n') for line in open(db)]

# 6 s3.id
# 7 Status
       klienti = Klienti.objects.all()
       count = 0

       for k in klienti:
           if len(k.card_nr) != 6:
               if len(k.card_nr) != 0:
                   count += 1
                   print k
                   print k.card_nr
  #len(k.card_nr)

       print count
