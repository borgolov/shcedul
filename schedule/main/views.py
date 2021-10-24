import json
from django.shortcuts import render
from django.template import Context, Template
from django.template.loader import get_template
from .models import *
from .service import *


# Create your views here.
def index(request):
    try:
        schedule, titl = screen_schedule(request)
        context = {'main': schedule, 'title': titl}
        return render(request, 'page.html', context)
    except:
        return render(request, 'error.html')
