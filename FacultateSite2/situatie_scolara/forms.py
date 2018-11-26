# situatie_scolara/forms.py
from django import forms
from .models import SituatieScolara, Materii
from django.forms import ModelForm
from accounts.models import Profesor

class AdaugareNoteForm(ModelForm):
    class Meta:
        model = SituatieScolara
        fields = ('nota', 'materia')

class SelectieMateriiForm(ModelForm):
    class Meta:
        model = Profesor
        fields = ('materia',)

class CreareGrupeForm(ModelForm):
    class Meta:
        model = Grpa
        fields = ('numarul', 'seria','materia')
