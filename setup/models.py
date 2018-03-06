# -*- coding: utf-8 -*-
from django.db import models


# !!!!! Apdrošinātāji !!!!!
class Apdrosinataji(models.Model):
    class Meta():
        db_table = "apdrosinataji"

    visible = models.BooleanField( default=False )
    title = models.CharField( max_length = 40, default = '' )

    def __unicode__(self):
        return u'%s' % (self.title)

# !!!!! Settingi !!!!!
class Settings(models.Model):
    class Meta():
        db_table = "settings"

    key = models.CharField( max_length = 40, default = '' )
    value = models.CharField( max_length = 100, blank = True )

    def __unicode__(self):
        return u'%s' % (self.key)


