# -*- coding: utf-8 -*-
from django.db import models

from django.utils import timezone
from django.contrib.auth.models import User


# !!!!! User login/logout !!!!!
class Login(models.Model):
    class Meta():
        db_table = "user_autorization"

    date = models.DateTimeField( default = timezone.now )
    ip = models.CharField( max_length = 20, default = '' )
    event = models.CharField( max_length = 10 )
    user = models.ForeignKey( User )


# !!!!! Report Log !!!!!
class Reports(models.Model):
    class Meta():
        db_table = "reports_log"

    date = models.DateTimeField( default = timezone.now )

    event = models.CharField( max_length = 100 )
    event_data = models.CharField( max_length = 200, default = '' )

    user = models.ForeignKey( User )
