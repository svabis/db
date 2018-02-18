# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect	# response to template, redirect to another view

from django.contrib import auth			# autorisation library
from django.contrib.auth.models import User, Group

from django.core.context_processors import csrf

from setup.models import Settings

from database.args import create_args

# !!!!! LOGIN !!!!!
def login(request):
    args = create_args(request)
    if args['access'] == False:
        return redirect (Settings.objects.get( key = "access denied redirect" ).value)

    args.update(csrf(request))      # encript data
    args['heading'] = "Sistēmas autorizācija"

    if request.POST:        # actions if login Form is submitted
        username = request.POST.get('username', '')      # usermname <= get variable from Form (name="username"), if not leave blank
        password = request.POST.get('password', '')      # password <= get variable from Form (name="password"), if not leave blank
        user = auth.authenticate( username = username, password = password ) # new variable --> user from auth system

        if user is not None: # auth return None if this user does not exit, if not then:
            auth.login( request, user ) # authorizate user from Form
           # clear COOKIES
            response = redirect ('/')
            response.delete_cookie('active_client')

            response.delete_cookie('edit_client')
            response.delete_cookie('new_client')
            return response


        else:   # if user does not exist:
            args['login_error']     = "Lietotājs nav atrasts"
            return render_to_response ( 'login.html', args )

    else:   # actions if activated hyperlink to login Form
        return render_to_response ( 'login.html', args )


# !!!!! LOG OUT !!!!!
def logout(request):
    auth.logout(request)
    response = redirect ('/login/')
    response.delete_cookie('active_client')

    response.delete_cookie('edit_client')
    response.delete_cookie('new_client')
    return response