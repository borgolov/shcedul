from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('schedule', get_schedule, name='schedule'),
    path('slider', slider, name='slider'),
    path('screensslider', get_slider, name='screensslider'),
    path('slidertime', get_slider_time, name='slidertime')
]