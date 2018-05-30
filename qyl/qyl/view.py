# -*- coding: utf-8 -*-

# from django.http import HttpResponse
from django.shortcuts import render
import os
from django.conf import settings
from django.http import HttpResponse
import zipfile
from django.http import StreamingHttpResponse

img_path = "/home/obe60/qyl_spider/img/"

def hello(request):

    try:
        id = request.GET["id"]
    except:
        id = "25539"

    img_dir = img_path + id
    if os.path.exists(img_dir):
        make_zip(img_path+id+"/","/home/obe60/"+id+".zip")
        print "zip success!"

        the_file_name = "/home/obe60/"+id+".zip"
        response = StreamingHttpResponse(file_iterator(the_file_name))
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment;filename="{0}"'.format(the_file_name)

        return response

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


def file_iterator(file_name, chunk_size=512):
    with open(file_name) as f:
        while True:
            c = f.read(chunk_size)
            if c:
                yield c
            else:
                break


