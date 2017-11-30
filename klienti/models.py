# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone


# !!! Klienti !!!
STATUS_CHOISE = (
    ('B', 'Biedrs'),
    ('S', 'Sudrabs'),
    ('Z', 'Zelts'),
    ('V', 'VIP'),
    ('D', 'Darbinieks')
)

GENDER_CHOISE = (
    ('V', 'Vīrietis'),
    ('S', 'Sieviete'),
)

class Klienti(models.Model):
    class Meta():
        db_table = "klienti"

    name = models.CharField( max_length = 40, default = '' )
    surname = models.CharField( max_length = 40, default = '' )

    avatar = models.ImageField( blank = True, null=True, upload_to = "client/" )

    birthday = models.DateField( blank = True, null = True ) #, default = timezone.now )
    phone = models.CharField( max_length=25, blank = True, null = True ) #default = '' )
    e_mail = models.EmailField ( blank = True, null = True )

    card_nr = models.CharField( max_length = 16, default = '', blank = True )

    card_blocked = models.BooleanField( default=False )
    client_blocked = models.BooleanField( default=False )

    status = models.CharField( max_length = 1, choices = STATUS_CHOISE )
    status_changed = models.BooleanField( default=False )
    society = models.BooleanField( default=False )

    gender = models.CharField( max_length = 1, choices = GENDER_CHOISE )

    reg_date = models.DateTimeField( default = timezone.now )

    notes = models.CharField( max_length = 150, default = '', blank = True )

    def __unicode__(self):
        return u'%s' % (self.name)


