# -*- coding: utf-8 -*-
import os       # for work with filesystem
import re       # for regular expresions (regex)

from clients.models import Klienti, Statusi

# progress bar
from tqdm import tqdm


# IMPORT DJANGO STUFF
from django.core.files import File	# for file opening

from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    def handle(self, *args, **options):

# 0 Person no
# 31 Status

       st = '/home/svabis/Tabulas/T00808Memo'

       counter = 0

       lines = [line.rstrip('\n') for line in open(st)]

       for i in tqdm( range( len(lines) ) ):
         l = lines[i].split('\t')

         if l[5] == "1-4666":
           temp = l[8].rstrip('\\x0d\\x0a')
           temp = temp.replace('\\x0d\\x0a', '\n')

#           if True:
           try:
               k = Klienti.objects.get( s3_nr = l[5] )
#               if k.notes != temp:
               k.notes = temp
               k.save()
#                   counter += 1

           except:
               pass
#               print l
#               memo.append( l )

       print "save:\t" + str( counter )
    #   print "errors:\t" + str( len(memo) )
