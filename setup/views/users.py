# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect

from django.core.context_processors import csrf

from database.args import create_args

# Lietotāji
from django.contrib.auth.models import User

# Setingi
from setup.models import Settings


#=================================================
# !!!!! Sistēmas lietotāji !!!!!
def system_users(request):
    args = create_args(request)
    if args['access'] == False:
        return redirect (Settings.objects.get( key = "access denied redirect" ).value)
    if args['loged_in'] == False:
        return redirect("/login/")
    if args['admin'] != True:
        return redirect("/login/")

    args.update(csrf(request)) # ADD CSRF TOKEN

    args['active_tab_7'] = True
    args['setup_tab_2'] = True

   # Lietotāji
    args['users'] = User.objects.all()

    return render_to_response ( 'users.html', args )


#=================================================
# !!!!! Izveidot Lietotāju !!!!!
def add_user(request):
    args = create_args(request)
    if args['access'] == False:
        return redirect (Settings.objects.get( key = "access denied redirect" ).value)
    if args['loged_in'] == False:
        return redirect("/login/")
    if args['admin'] != True:
        return redirect("/login/")

    args.update(csrf(request)) # ADD CSRF TOKEN

#    if request.POST:
#        

    return render_to_response ( 'users.html', args )
