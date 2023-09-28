from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(ProfileCategory)
admin.site.register(DoctorProfile)
admin.site.register(Doctor)
admin.site.register(ScheduleType)
admin.site.register(Schedule)
admin.site.register(Screen)
admin.site.register(Slider)