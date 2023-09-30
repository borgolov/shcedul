from .models import *


def get_screen(id):
    return Screen.objects.get(id=id)


def get_schedules(screen: Screen) -> Screen:
    return screen.schedule.all()


def get_slider_on_id(id):
    return Slider.objects.get(id=id)


def get_profiles_in_schedules(screen: Screen):
    schedules = get_schedules(screen)
    profiles = []
    for s in schedules:
        profiles.append(s.doctor.profile.category)
    profiles_clear = []
    [profiles_clear.append(x) for x in profiles if x not in profiles_clear]
    return profiles_clear


def create_schema(screen: Screen):
    lista = get_profiles_in_schedules(screen)
    schema = list()
    for item in lista:
        item_js = {"profile_type": item.name, "rows": []}
        for i in get_schedules(screen):
            if i.doctor.profile.category == item:
                sc = {
                    'doc': i.doctor.family + " " + i.doctor.name + " " + i.doctor.middle,
                    'room': i.room,
                    'profile': i.doctor.profile.name,
                    'monday': i.monday,
                    'tuesday': i.tuesday,
                    'wednesday': i.wednesday,
                    'thursday': i.thursday,
                    'friday': i.friday,
                    'saturday': i.saturday,
                    'sunday': i.sunday,
                    'is_holiday': i.is_holiday,
                    'type': i.schedule_type.name,
                }
                item_js['rows'].append(sc)
        schema.append(item_js)
    return schema


def screen_schedule(request):
    screen = get_screen(request.GET.get('screen_id'))
    lista = get_profiles_in_schedules(screen)
    schema = create_schema(screen)
    return schema, screen.title


def slider_schedule(request):
    slider: Slider = get_slider_on_id(request.GET.get('slider_id'))
    screens = slider.screens.all()
    schema = list()
    for item in screens:
        schema.append(create_schema(item))
    return schema


def get_timer_slide_on_id(slider_id):
    slider: Slider = get_slider_on_id(slider_id)
    return slider.time_for_slide



