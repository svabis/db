# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User

# !!! StatusType !!!
class Statusi(models.Model):
    class Meta():
        db_table = "status_type"

    status_name = models.CharField( max_length = 40, default = '' )
    status_discount = models.CharField( max_length = 5, default = '' )

    def __unicode__(self):
        return u'%s' % (self.status_name)


# !!! Klienti !!!
GENDER_CHOISE = ( ('V', 'Vīrietis'), ('S', 'Sieviete') )

class Klienti(models.Model):
    class Meta():
        db_table = "klienti"

   # ID FROM S3 DATABASE FOR BINDING KLIENTS, IMAGES, NOTES E.T.C.
    s3_nr = models.CharField( max_length = 10, default = '' )

    name = models.CharField( max_length = 40, default = '' )
    surname = models.CharField( max_length = 40, default = '' )

    avatar = models.ImageField( blank = True, null=True, upload_to = "client/" )

    first = models.BooleanField( default=False ) # apmeklējis jau kaut ko

    frozen = models.BooleanField( default=False ) # iesaldēts
    frozen_from = models.DateField( blank = True, null = True )
    frozen_until = models.DateField( blank = True, null = True )


    birthday = models.DateField( blank = True, null = True )
    phone = models.CharField( max_length = 30, blank = True, null = True )
    e_mail = models.EmailField ( blank = True, null = True )

    card_nr = models.CharField( max_length = 16, default = '', blank = True )

    card_blocked = models.BooleanField( default=False )
    client_blocked = models.BooleanField( default=False )

    status = models.ForeignKey( Statusi )
    status_changed = models.BooleanField( default=False )
    society = models.BooleanField( default=False ) # "biedrība"

    gender = models.CharField( max_length = 1, choices = GENDER_CHOISE )

    reg_date = models.DateTimeField( default = timezone.now ) # registration

    disabled = models.BooleanField( default=False ) # invalīds
    disabled_until = models.DateField( blank = True, null = True )
    student = models.BooleanField( default=False ) # skolnieks/students
    student_until = models.DateField( blank = True, null = True )
    elderly = models.BooleanField( default=False ) # pensionārs

    notes = models.CharField( max_length = 500, default = '', blank = True )

    def __unicode__(self):
        return self.name + " " + self.surname


# !!!!! Blacklist !!!!!
class Blacklist(models.Model):
    class Meta():
        db_table = "blacklist"

    bl_user = models.ForeignKey( User, default = 1 )

    bl_client = models.ForeignKey( Klienti )
    bl_date = models.DateTimeField( default = timezone.now )
    bl_data = models.CharField( max_length = 300 )

    def __unicode__(self):
        return u'%s' % (self.bl_user)


# !!!!! Depozīts !!!!!
class Deposit(models.Model):
    class Meta():
        db_table = "depozits"

    d_user = models.ForeignKey( User, default = 1 )

    d_client = models.ForeignKey( Klienti )
    d_date = models.DateTimeField( default = timezone.now )
    d_amount = models.DecimalField( max_digits = 5, decimal_places = 2 )
