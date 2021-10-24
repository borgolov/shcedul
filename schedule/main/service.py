from .models import *


def get_screen(id):
    return Screen.objects.get(id=id)


def get_schedules(screen: Screen) -> Screen:
    return screen.schedule.all()


def get_profiles_in_schedules(screen: Screen):
    schedules = get_schedules(screen)
    profiles = []
    for s in schedules:
        profiles.append(s.doctor.profile.category)
    profiles_clear = []
    [profiles_clear.append(x) for x in profiles if x not in profiles_clear]
    return profiles_clear


def screen_schedule(request):
    screen = get_screen(request.GET.get('screen_id'))
    lista = get_profiles_in_schedules(screen)
    schema = list()
    for item in lista:
        item_js = {"category": item.name, "schedules": []}
        for i in get_schedules(screen):
            if i.doctor.profile.category == item:
                sc = {
                    'doctor': i.doctor.family + " " + i.doctor.name + " " + i.doctor.middle,
                    'room': i.room,
                    'monday': i.monday
                }
                item_js['schedules'].append(i)
        schema.append(item_js)
    return schema, screen.title




