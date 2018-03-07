# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone

# Django useri
from django.contrib.auth.models import User

from datetime import datetime

from clients.models import Klienti # abonementa īpašnieks

from setup.models import Apdrosinataji

# ???
def default_start_time():
    now = datetime.now()
    start = now.replace(hour=8, minute=0, second=0, microsecond=0)
    return start

# =========================================================================
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


# =========================================================================
# !!! SUBSCRIPTION_TYPES !!!
class AbonementType(models.Model):
    class Meta():
        db_table = "abonementu_tipi"

    title = models.CharField( max_length = 100, default = '' ) # nosaukums

    created = models.DateTimeField( default = timezone.now ) # izveidots

    available = models.BooleanField( default=True ) # pašlaik pieejams

    discount = models.BooleanField( default=True ) # atlaide

    short_title = models.CharField( max_length = 100, default = '' ) # saīsinātais nosaukums ar HTML tagiem priekš izvēles sadaļas

    position = models.IntegerField( blank = True, null = True ) # novietojums izvēles sadaļā
    position1 = models.IntegerField( blank = True, null = True ) # novietojums izvēles sadaļā

    price = models.DecimalField( max_digits = 5, decimal_places = 2 ) # cena

    special = models.BooleanField( default=False ) # speciālie abonementi
    extra = models.BooleanField( default=False ) # īpašie abonementi

    first_time = models.BooleanField( default=False ) # iepazīšanās

    activate_before = models.IntegerField( blank = True, null = True, default = 1 ) # derīgs līdz (mēneši)
    best_before = models.IntegerField( blank = True, null = True ) # derīgs līdz (mēneši)

    time_limit = models.BooleanField( default=False ) # laika limits (rīti, darbadienas u.t.t.)
    time_limit_type =  models.ForeignKey( TimelimitType, blank=True, null=True ) # laika limita relācija (ja tāda ir)

    times = models.BooleanField( default=False ) # reižu limits
    times_count = models.IntegerField( blank = True, null = True ) # reižu skaits

    s3_nr = models.CharField( max_length = 10, default = '' )

    def __unicode__(self):
        return u'%s' % (self.title)


# =========================================================================
# !!! SUBSCRIPTION_TYPES !!!
class Abonementi(models.Model):
    class Meta():
        db_table = "abonementi"

    user = models.ForeignKey( User, default = 1 ) # abonementa īpašnieks

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


# =========================================================================
# !!! pirkums !!!
class Abonementu_Apmaksa(models.Model):
    class Meta():
        db_table = "abonementi_pirkums"

    date = models.DateTimeField( default = timezone.now ) # pirkuma datums
    user = models.ForeignKey( User, default = 1 ) # abonementa īpašnieks
#---
    client = models.ForeignKey( Klienti ) # abonementa īpašnieks
    subscr = models.ForeignKey( Abonementi ) # iegādātais abonements
#---
    full_price = models.DecimalField( max_digits = 5, decimal_places = 2 ) # pilnā cena
    discount_price = models.DecimalField( max_digits = 5, decimal_places = 2 ) # cena ar atlaidi
#---
    from_deposit = models.DecimalField( max_digits = 5, decimal_places = 2 ) # summa no depozīta
#---
    from_gift_card = models.DecimalField( max_digits = 5, decimal_places = 2 ) # summa no dāvanu kartes
#---
    insurance = models.ForeignKey( Apdrosinataji, blank=True, null=True ) # apdrošinātājs
    insurance_cash = models.DecimalField( max_digits = 5, decimal_places = 2 ) # sedz apdrošinātājs
#---
    cash = models.BooleanField( default = False ) # skaidra nauda
    card = models.BooleanField( default = False ) # kredītkarte
    transfer = models.BooleanField( default = False ) # pārskaitījums
#---
#    additonal_discount = models.BooleanField( default = False ) # papildus atlaide
    final_price = models.DecimalField( max_digits = 5, decimal_places = 2 ) # gala cena

    def __unicode__(self):
        return u'%s' % (self.date)
