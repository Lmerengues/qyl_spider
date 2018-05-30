# -*- coding: utf-8 -*-

# from django.http import HttpResponse
from django.shortcuts import render
import os
from django.conf import settings
from django.http import HttpResponse

def hello(request):

    if os.path.exists("/home/obe60/qyl_spider/img/25249"):
        return HttpResponse("1")
    else:
        return HttpResponse("0")
