# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect

from django.contrib import auth # autorisation library
from django.contrib.auth.models import User, Group

from django.core.context_processors import csrf

from database.args import create_args

# Klienta modelis
from klienti.models import Klienti



# !!!!! MAIN VIEW !!!!!
def main(request):
    args = create_args(request)
    args.update(csrf(request))      # ADD CSRF TOKEN

    args['active_tab_1'] = True

    if request.POST:
        id = request.POST.get('id', '')
        if id == "14083":
            args['client'] = Klienti.objects.all()[0]

        if id == "1":
            args['client'] = Klienti.objects.all()[1]

        if id == "2":
            args['client'] = Klienti.objects.all()[2]

        if id == "3":
            args['client'] = Klienti.objects.all()[4]

        if id == "klblok":
            args['client'] = Klienti.objects.all()[2]
            args['error'] = True
            args['error_code_3'] = True

        if id == "cblok":
            args['client'] = Klienti.objects.all()[2]
            args['error'] = True
            args['error_code_2'] = True

        if id == "er":
            args['error'] = True
            args['error_code_1'] = True


    return render_to_response ( 'main_content.html', args )
