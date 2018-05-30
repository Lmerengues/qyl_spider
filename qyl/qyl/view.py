# -*- coding: utf-8 -*-

# from django.http import HttpResponse
from django.shortcuts import render
import os
from django.conf import settings
from django.http import HttpResponse


def hello(request):

    if os.path.exists("/static/test.png"):
        return HttpResponse("1")
    else:
        return HttpResponse("0")
