from django.db import models
from accounts.models import Student, Profesor
# Create your models here.

class Materii(models.Model):
    nume = models.CharField(blank=True, max_length=100)
    semestru = models.IntegerField(blank=True, null=True)
    puncte_credit = models.IntegerField(blank=True, null=True)
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)

class SituatieScolara(models.Model):
    nota = models.IntegerField(blank=True, null=True)
    materia = models.ForeignKey(Materii, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    admis = models.BooleanField(default=False)
