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

SEX_CHOISE = (
    ('V', 'Vīrietis'),
    ('S', 'Sieviete'),
)

class Klienti(models.Model):
    class Meta():
        db_table = "klienti"

    name = models.CharField( max_length = 15, default = '' )
    surname = models.CharField( max_length = 15, default = '' )

    avatar = models.ImageField( blank = True, null=True, upload_to = "client/" )

    birthday = models.DateField( default = timezone.now )
    phone = models.CharField( max_length=16, default = '' )
    e_mail = models.EmailField ()

    card_nr = models.CharField( max_length = 16, default = '', blank = True )

    card_blocked = models.BooleanField( default=False )
    client_blocked = models.BooleanField( default=False )

    status = models.CharField( max_length = 1, choices = STATUS_CHOISE )
    sex = models.CharField( max_length = 1, choices = SEX_CHOISE )

    reg_date = models.DateTimeField( default = timezone.now )

    notes = models.CharField( max_length = 150, default = '', blank = True )

    def __unicode__(self):
        return u'%s' % (self.name)


