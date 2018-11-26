# situatie_scolara/forms.py
from django import forms
from .models import SituatieScolara, Materii, Grupa, MateriiGrupa
from django.forms import ModelForm
from accounts.models import Profesor , Student

class AdaugareNoteForm(ModelForm):
    class Meta:
        model = SituatieScolara
        fields = ('nota', 'materia')

class MateriiGrupaForm(ModelForm):
    class Meta:
        model = MateriiGrupa
        fields = ('materie', )

class StudentInfoForm(ModelForm):
    class Meta:
        model = Student
        fields = ('nume','prenume', )

class SelectieMateriiForm(ModelForm):
    class Meta:
        model = Profesor
        fields = ('materia',)

class CreareGrupeForm(ModelForm):
    class Meta:
        model = Grupa
        fields = ('numarul', 'seria','materia')
