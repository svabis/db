# -*- coding: utf-8 -*-
from django.db import models

# !!! SUBSCRIPTION !!!
class Abonementi(models.Model):
    class Meta():
        db_table = "abonementi"

    title = models.CharField( max_length = 60, default = '' ) # nosaukums
    price = models.DecimalField( max_digits = 5, decimal_places = 2 ) # cena

    special = models.BooleanField( default=False ) # īpašie abonementi

    first_time = models.BooleanField( default=False ) # iepazīšanās

    best_before = models.IntegerField( blank = True, null = True ) # derīgs līdz (mēneši * 30)

    time_limit = models.BooleanField( default=False ) # laika limits (rīti, darbadienas u.t.t.)

    times = models.BooleanField( default=False ) # reižu limits
    times_count = models.IntegerField( blank = True, null = True ) # reižu skaits

    def __unicode__(self):
        return u'%s' % (self.title)
