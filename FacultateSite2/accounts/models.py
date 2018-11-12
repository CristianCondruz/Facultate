from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class CustomUser(AbstractUser):
    # add additional fields in here
    is_student = models.BooleanField(default=False)
    def __str__(self):
        return self.username

class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=True, related_name='student')
    grupa = models.CharField(blank=True, max_length=100)
    an = models.IntegerField(blank=True, null=True)
    media_generala = models.FloatField(blank=True, null=True)
    nr_credite = models.IntegerField(blank=True, null=True)
    nume = models.CharField(blank=True, max_length=100)
    prenume = models.CharField(blank=True, max_length=100)
    data_nastere = models.DateField(blank=True, null=True)
    adresa_domiciliu = models.CharField(blank=True, max_length=100)
    cnp = models.IntegerField(blank=True, null=True)
    facebook_site = models.URLField(blank=True)
    linkedin_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to = 'profile_pics', blank=True)


    def __str__(self):
        return self.nume

class Profesor(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=True, related_name='profesor')
    nume = models.CharField(blank=True, max_length=100)
    prenume = models.CharField(blank=True, max_length=100)
    grad = models.CharField(blank=True, max_length=100)
    facebook_site = models.URLField(blank=True)
    linkedin_site = models.URLField(blank=True)
    research_gate_profile = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to = 'profile_pics', blank=True)

    def __str__(self):
        return self.nume

@receiver(post_save, sender=CustomUser)
def user_is_created(sender, instance, created, **kwargs):
    if instance.is_student:
        if created:
            Student.objects.create(user = instance)
        else:
            instance.student.save()
    else:
        if created:
            print("professor")
            Profesor.objects.create(user = instance)
        else:
            instance.profesor.save()
