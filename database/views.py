# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect

from django.contrib import auth # autorisation library
from django.contrib.auth.models import User, Group

from django.core.context_processors import csrf

from database.args import create_args

# !!!!! MAIN VIEW !!!!!
def main(request):
    args = create_args(request)

    args['active_tab_1'] = True

    return render_to_response ( 'main_content.html', args )
