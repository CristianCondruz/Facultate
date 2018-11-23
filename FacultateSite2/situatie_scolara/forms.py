# situatie_scolara/forms.py
from django import forms
from .models import SituatieScolara, Materii
from django.forms import ModelForm

class AdaugareNoteForm(ModelForm):
    class Meta:
        model = SituatieScolara
        fields = ('nota', 'materia')

class SelectieMateriiForm(ModelForm):

    class Meta:
        model = Materii
        fields = ('nume','semestru')
