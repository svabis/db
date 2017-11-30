# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone

from klienti.models import Klienti

GENDER_CHOISE = (
    ('V', 'Vīrietis'),
    ('S', 'Sieviete'),
)

class Skapji(models.Model):
    class Meta():
        db_table = "skapji"

    number = models.CharField( max_length = 3 )

    locker_type = models.CharField( max_length = 1, choices = GENDER_CHOISE )

    checkin_time = models.DateTimeField( default = timezone.now )

    client = models.ForeignKey( Klienti , related_name='locker_client' )

    def __unicode__(self):
        return u'%s' % (self.number)


