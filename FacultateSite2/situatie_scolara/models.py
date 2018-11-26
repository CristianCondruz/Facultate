from django.db import models
# Create your models here.

class Materii(models.Model):
    nume = models.CharField(blank=True, max_length=100)
    semestru = models.IntegerField(blank=True, null=True)
    puncte_credit = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.nume

class Grupa(models.Model):
    numarul = models.IntegerField(blank=True, null=True)
    seria = models.CharField(blank=True, null=True, max_length=1)
    materia = models.ManyToManyField(Materii, through='MateriiGrupa')
    def __str__(self):
        return str(self.numarul)

class MateriiGrupa(models.Model):
    materie = models.ForeignKey(Materii, related_name='materie',on_delete='cascade')
    grupa = models.ForeignKey(Grupa, related_name='grupa',on_delete='cascade')
    def __str__(self):
        return self.materie, self.grupa

class SituatieScolara(models.Model):
    nota = models.IntegerField(blank=True, null=True)
    materia = models.ForeignKey(Materii, on_delete=models.CASCADE)
    admis = models.BooleanField(default=False)
