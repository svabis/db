# -*- coding: utf-8 -*-
from django.contrib.auth.models import User	# autorisation library
from django.contrib import auth			# autorisation library


# !!!!! IP GRABBER !!!!!
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


# !!! Apkopots args !!!
def create_args(request):
    args = {}
    args['ip'] = get_client_ip(request)
    args['help'] = False
    args['django'] = True
    return args

