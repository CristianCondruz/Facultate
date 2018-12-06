from django.db import models
from situatie_scolara.models import Materii

DAY_OF_THE_WEEK = {
    '1' : (u'Monday'),
    '2' : (u'Tuesday'),
    '3' : (u'Wednesday'),
    '4' : (u'Thursday'),
    '5' : (u'Friday'),
    '6' : (u'Saturday'),
    '7' : (u'Sunday'),
}
INTERVALUL_ORAR = {
    '1' : (u'8-10'),
    '2' : (u'10-12'),
    '3' : (u'12-14'),
    '4' : (u'14-16'),
    '5' : (u'16-18'),
    '6' : (u'18-20'),
    '7' : (u'20-22'),
}

class DayOfTheWeekField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs['choices']=tuple(sorted(DAY_OF_THE_WEEK.items()))
        kwargs['max_length']=1
        super(DayOfTheWeekField,self).__init__(*args, **kwargs)
class IntervalOrarField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs['choices']=tuple(sorted(INTERVALUL_ORAR.items()))
        kwargs['max_length']=1
        super(IntervalOrarField,self).__init__(*args, **kwargs)

# Create your models here.
class Locatii(models.Model):
    corpul = models.CharField(blank=True, max_length=100)
    sala = models.CharField(blank=True, max_length=100)

    def __str__(self):
        return "%s %s" % (self.corpul, self.sala)

class Orar(models.Model):
    ziua_saptamanala = DayOfTheWeekField(blank=True)
    locatia = models.ForeignKey(Locatii,on_delete='cascade')
    materia = models.ForeignKey(Materii,on_delete='cascade')
    anul = models.CharField(blank=True, max_length=100)
    tip = models.CharField(blank=True, max_length=100)
    intervalul_orar = IntervalOrarField(blank=True)

    def __str__(self):
        return "%s %s %s %s %s %s" % (self.ziua_saptamanala, self.locatia, self.materia, self.anul, self.tip,self.intervalul_orar)
