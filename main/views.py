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
                      {'title': 'ОГБУЗ "Иркутская городская клиническая больница №3"', 'list': Screen.objects.all(), 'list_slider': Slider.objects.all()})


def get_schedule(request):
    schedule, titl = screen_schedule(request)
    context = schedule
    return JsonResponse({'response': context})


def slider(request):
    slider_id = request.GET.get('slider_id')
    slider: Slider = get_slider_on_id(slider_id)
    return render(request, 'slider.html', {'title': slider.title})


def get_slider(request):
    context = slider_schedule(request)
    return JsonResponse({'response': context})


def get_slider_time(request):
    slider_id = request.GET.get('slider_id')
    time = get_timer_slide_on_id(slider_id)
    return JsonResponse({'response': time})