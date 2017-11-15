# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect

from django.contrib import auth # autorisation library
from django.contrib.auth.models import User, Group

from django.core.context_processors import csrf


def main(request):
    args = {}
    args['help'] = False
    args['django'] = True
    return render_to_response ( 'main_head.html', args )
