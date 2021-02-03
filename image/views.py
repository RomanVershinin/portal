from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from . import models

def get_all_image(request):
    return HttpResponse('All image')
