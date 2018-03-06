# -*- coding: utf-8 -*-
from django.db import models


class Apdrosinataji(models.Model):
    class Meta():
        db_table = "apdrosinataji"

    visible = models.BooleanField( default=False )
    title = models.CharField( max_length = 40, default = '' )


class Settings(models.Model):
    class Meta():
        db_table = "settings"

    key = models.CharField( max_length = 40, default = '' )
    value = models.CharField( max_length = 100, blank = True )

    def __unicode__(self):
        return u'%s' % (self.key)


