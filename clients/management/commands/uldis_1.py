# -*- coding: utf-8 -*-
import os       # for work with filesystem
import re       # for regular expresions (regex)
import datetime # for file create field
import pytz	# to set timezone

from subscriptions.models import AbonementType

from datetime import datetime

# progress bar
from tqdm import tqdm

from django.core.files import File	# for file opening

# IMPORT DJANGO STUFF
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    def handle(self, *args, **options):

       file = open("../abon.txt","w")

       abon = AbonementType.objects.all()

       for i in tqdm( range( abon.count() ) ):
           file.write( str( abon[i].id ) + "\t" + str(abon[i]) )

       file.close()
