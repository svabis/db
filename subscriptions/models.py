# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone

from datetime import datetime

from clients.models import Klienti # abonementa īpašnieks

def default_start_time():
    now = datetime.now()
    start = now.replace(hour=8, minute=0, second=0, microsecond=0)
    return start

# !!! TIMELIMIT_TYPE !!!
class TimelimitType(models.Model):
    class Meta():
        db_table = "laika_limiti_tipi"

    title = models.CharField( max_length = 60, default = '' )

    weekday1 = models.BooleanField( default=False )

    weekday1_start_time = models.TimeField( blank=True, null=True )
    weekday1_end_time = models.TimeField( blank=True, null=True )

    weekday2 = models.BooleanField( default=False )

    weekday2_start_time = models.TimeField( blank=True, null=True )
    weekday2_end_time = models.TimeField( blank=True, null=True )

    weekend = models.BooleanField( default=False )

    weekend_start_time = models.TimeField( blank=True, null=True )
    weekend_end_time = models.TimeField( blank=True, null=True )

    def __unicode__(self):
        return u'%s' % (self.title)


# !!! SUBSCRIPTION_TYPES !!!
class AbonementType(models.Model):
    class Meta():
        db_table = "abonementu_tipi"

    title = models.CharField( max_length = 60, default = '' ) # nosaukums

    available = models.BooleanField( default=True ) # pašlaik pieejams

    short_title = models.CharField( max_length = 60, default = '' ) # saīsinātais nosaukums ar HTML tagiem priekš izvēles sadaļas
    position = models.IntegerField( blank = True, null = True ) # novietojums izvēles sadaļā

    price = models.DecimalField( max_digits = 5, decimal_places = 2 ) # cena

    special = models.BooleanField( default=False ) # īpašie abonementi

    first_time = models.BooleanField( default=False ) # iepazīšanās

    best_before = models.IntegerField( blank = True, null = True ) # derīgs līdz (mēneši)

    time_limit = models.BooleanField( default=False ) # laika limits (rīti, darbadienas u.t.t.)
    time_limit_type =  models.ForeignKey( TimelimitType, blank=True, null=True ) # laika limita relācija (ja tāda ir)

    times = models.BooleanField( default=False ) # reižu limits
    times_count = models.IntegerField( blank = True, null = True ) # reižu skaits

    def __unicode__(self):
        return u'%s' % (self.title)


# !!! SUBSCRIPTION_TYPES !!!
class Abonementi(models.Model):
    class Meta():
        db_table = "abonementi"

    active = models.BooleanField( default = False ) # aktivējot mainās uz True
    ended = models.BooleanField( default = False ) # ja beidzās, tad mainās uz True

    client = models.ForeignKey( Klienti ) # abonementa īpašnieks

    subscr = models.ForeignKey( AbonementType ) # abonements

    price = models.DecimalField( max_digits = 5, decimal_places = 2 ) # cena

    purchase_date = models.DateTimeField( default = timezone.now ) # pirkuma datums (izmantošanas secībai)

    activation_date = models.DateTimeField( blank = True, null = True ) # aktivācijas laiks
    activate_before = models.DateTimeField( blank = True, null = True ) # derīgs aktivācijai līdz

    best_before = models.DateTimeField( blank = True, null = True ) # derīgs līdz (laiks/datums, rēķinās aktivācijas diena/laiks + timedelta month no AbonementType)

    times_count = models.IntegerField( blank = True, null = True ) # atlikušo reižu skaits, ja ir

    def __unicode__(self):
        return u'%s' % (self.subscr)
