# -*- coding: utf-8 -*-
from django.contrib.auth.models import User	# autorisation library


# !!! Apkopots args !!!
def create_args(request):
    args = {}
    args['help'] = False
    args['django'] = True
    return args

