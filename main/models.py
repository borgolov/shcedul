from django.db import models


# Create your models here.
class ProfileCategory(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория профилей'
        verbose_name_plural = 'Категории профилей'


class DoctorProfile(models.Model):
    name = models.CharField(max_length=30)
    category = models.ForeignKey(ProfileCategory, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Профиль врача'
        verbose_name_plural = 'Профили врачей'


class Doctor(models.Model):
    family = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    middle = models.CharField(max_length=50)
    profile = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.family + " " + self.name + " " + self.middle

    class Meta:
        verbose_name = 'Врач'
        verbose_name_plural = 'Врачи'


class ScheduleType(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Вид очереди'
        verbose_name_plural = 'Виды очередей'


class Schedule(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    monday = models.CharField(max_length=20, blank=True)
    tuesday = models.CharField(max_length=20, blank=True)
    wednesday = models.CharField(max_length=20, blank=True)
    thursday = models.CharField(max_length=20, blank=True)
    friday = models.CharField(max_length=20, blank=True)
    saturday = models.CharField(max_length=20, blank=True)
    sunday = models.CharField(max_length=20, blank=True)
    room = models.CharField(max_length=20, blank=True)
    schedule_type = models.ForeignKey(ScheduleType, on_delete=models.CASCADE)
    is_holiday = models.BooleanField()

    def __str__(self):
        return self.doctor.family + " " + self.doctor.name + " " + self.doctor.middle

    class Meta:
        verbose_name = 'Расписание'
        verbose_name_plural = 'Расписания'


class Screen(models.Model):
    name = models.CharField(max_length=30)
    title = models.CharField(max_length=100, blank=True)
    schedule = models.ManyToManyField(Schedule, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Экран'
        verbose_name_plural = 'Экраны'


class Slider(models.Model):
    name = models.CharField(max_length=30)
    title = models.CharField(max_length=100, blank=True)
    screens = models.ManyToManyField(Screen, blank=True)
    time_for_slide = models.IntegerField(default=10, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Слайд экранов'
        verbose_name_plural = 'Слайды экранов'