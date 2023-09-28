import json
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.template import Context, Template
from django.template.loader import get_template
from .models import *
from .service import *


# Create your views here.
def index(request):
    scr_id = request.GET.get('screen_id')
    if scr_id:
        screen = get_screen(scr_id)
        return render(request, 'index_old.html', {'title': screen.title})
    else:
        return render(request, 'selector.html',
                      {'title': 'ОГБУЗ "Иркутская городская клиническая больница №3"', 'list': Screen.objects.all()})


def get_schedule(request):

    schedule, titl = screen_schedule(request)
    context = schedule
    return JsonResponse({'response': context})


def slider(request):
    slider_id = request.GET.get('slider_id')
    return(request, 'slider.html')