# -*- coding: utf-8 -*-
import os       # for work with filesystem
import re       # for regular expresions (regex)
import datetime # for file create field
import pytz	# to set timezone

from slugify import slugify

# progress bar
from tqdm import tqdm

from django.core.files import File	# for file opening

# IMPORT DJANGO STUFF
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    def handle(self, *args, **options):
       db = '/home/svabis/Tabulas/T00801Person'
       lines = [line.rstrip('\n') for line in open(db)]

# 0 Person no
# 5 First name
# 6 Surname
       file = open("../personen","w")

       for i in tqdm( range(len(lines)) ):
           l = lines[i].split('\t')
           file.write( l[0] + "\t" + slugify(l[5]) + "-" + slugify(l[6]) )

       file.close()
