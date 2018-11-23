# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Student, Profesor
from django.forms import ModelForm
from situatie_scolara.models import Materii

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ('nume', 'prenume', 'data_nastere', 'adresa_domiciliu', 'cnp', 'grupa', 'an' , 'profile_pic',
                                        'facebook_site', 'linkedin_site',  )

class ProfesorForm(ModelForm):
    class Meta:
        model = Profesor
        fields = ('nume','prenume','grad', 'profile_pic','facebook_site', 'linkedin_site', 'research_gate_profile')
