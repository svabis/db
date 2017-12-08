# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone

from clients.models import Klienti # abonementa īpašnieks

# !!! SUBSCRIPTION_TYPES !!!
class AbonementType(models.Model):
    class Meta():
        db_table = "abonementu_tipi"

    title = models.CharField( max_length = 60, default = '' ) # nosaukums

    short_title = models.CharField( max_length = 60, default = '' ) # saīsinātais nosaukums ar HTML tagiem priekš izvēles sadaļas
    position = models.IntegerField( blank = True, null = True ) # novietojums izvēles sadaļā

    price = models.DecimalField( max_digits = 5, decimal_places = 2 ) # cena

    special = models.BooleanField( default=False ) # īpašie abonementi

    first_time = models.BooleanField( default=False ) # iepazīšanās

    best_before = models.IntegerField( blank = True, null = True ) # derīgs līdz (mēneši)

    time_limit = models.BooleanField( default=False ) # laika limits (rīti, darbadienas u.t.t.)

    times = models.BooleanField( default=False ) # reižu limits
    times_count = models.IntegerField( blank = True, null = True ) # reižu skaits

    def __unicode__(self):
        return u'%s' % (self.title)


# !!! SUBSCRIPTION_TYPES !!!
class Abonementi(models.Model):
    class Meta():
        db_table = "abonementi"

    client = models.ForeignKey( Klienti ) # abonementa īpašnieks

    title = models.CharField( max_length = 60, default = '' ) # nosaukums
    price = models.DecimalField( max_digits = 5, decimal_places = 2 ) # cena

    purchase_date = models.DateTimeField( default = timezone.now ) # pirkuma datums (izmantošanas secībai)

    active = models.BooleanField( default=True ) # ja beidzās, tad mainās uz False

# LAIKAM NAV VAJADZĪGS
#    special = models.BooleanField( default=False ) # īpašie abonementi

    first_time = models.BooleanField( default=False ) # iepazīšanās (ja ir tāds tad otru pirkt --> DENIED)

    best_before = models.DateTimeField( blank = True, null = True ) # derīgs līdz (laiks/datums, rēķinās pirkšanas diena/laiks + timedelta month no AbonementType)

# FOREIGN KEY UZ KURŠ ???
#    time_limit = models.BooleanField( default=False ) # laika limits (rīti, darbadienas u.t.t.)

    times = models.BooleanField( default=False ) # reižu limits
    times_count = models.IntegerField( blank = True, null = True ) # atlikušo reižu skaits

    def __unicode__(self):
        return u'%s' % (self.title)
