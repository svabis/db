# -*- coding: utf-8 -*-
from django.db import models


class Settings(models.Model):
    class Meta():
        db_table = "settings"

    key = models.CharField( max_length = 40, default = '' )
    value = models.CharField( max_length = 40, default = '' )

    def __unicode__(self):
        return u'%s' % (self.key)


