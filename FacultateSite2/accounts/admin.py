from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Student, Profesor, ProfesorMateria
from situatie_scolara.models import Materii, SituatieScolara, Grupa, MateriiGrupa

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username',]

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Student)
admin.site.register(Profesor)
admin.site.register(Materii)
admin.site.register(Grupa)
admin.site.register(ProfesorMateria)
admin.site.register(MateriiGrupa)
