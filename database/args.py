# -*- coding: utf-8 -*-
from django.contrib.auth.models import User, Group  # autorisation library
from django.contrib import auth		    # autorisation library


from setup.models import Settings

from lockers.models import Skapji

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
    ip = get_client_ip(request)
    args['ip'] = ip # GET IP


   # get allowed IP address list and create True or False
    ip_list = Settings.objects.filter( key = "allowed access from ip" ) #.value
    alowed_ip = []
    for n in ip_list:
        alowed_ip.append( n.value )

    if ip in alowed_ip:
        args['access'] = True
    else:
        args['access'] = False
#    args['access'] = True

    args['loged_in'] = True
    args['admin'] = False
   # User not logged in
    if auth.get_user(request).get_username() == '': # IF NO USER -->
        args['loged_in'] = False

   # SUPERUSER
    username = auth.get_user(request)
    if username.is_superuser:
        args['django'] = True
        args['admin'] = True

   # GROUP --> "administrator"
    if username.groups.filter(name='administrator').exists():
        args['admin'] = True

    args['username'] = username
    args['help'] = True

   # In Club count
    args['in_club_count'] = Skapji.objects.all().count()
    return args

