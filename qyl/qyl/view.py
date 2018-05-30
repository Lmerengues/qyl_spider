# -*- coding: utf-8 -*-

# from django.http import HttpResponse
from django.shortcuts import render
import os
from django.conf import settings
from django.http import HttpResponse
import zipfile

img_path = "/home/obe60/qyl_spider/img/"

def hello(request):

    try:
        id = request.GET["id"]
    except:
        id = "25539"

    img_dir = img_path + id
    if os.path.exists(img_dir):
        make_zip(img_path,"/home/obe60/"+id+".zip")
        with open("/home/obe60/"+id+".zip") as f:
            c = f.read()
        return HttpResponse(c)
    else:
        return HttpResponse("error occurred!")



def make_zip(source_dir, output_filename):
    zipf = zipfile.ZipFile(output_filename, 'w')
    pre_len = len(os.path.dirname(source_dir))
    for parent, dirnames, filenames in os.walk(source_dir):
        for filename in filenames:
            pathfile = os.path.join(parent, filename)
            arcname = pathfile[pre_len:].strip(os.path.sep)
            zipf.write(pathfile, arcname)
    zipf.close()


