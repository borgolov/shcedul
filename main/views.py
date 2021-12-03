import json
from django.shortcuts import render
from django.http import JsonResponse
from django.template import Context, Template
from django.template.loader import get_template
from .models import *
from .service import *


# Create your views here.
def index(request):
    screen = get_screen(request.GET.get('screen_id'))
    if screen is None:
        return "404"
    else:
        return render(request, 'index.html', {'title': screen.title})


def get_schedule(request):

    schedule, titl = screen_schedule(request)
    context = schedule
    return JsonResponse({'response': context})