# situatie_scolara/forms.py
from django import forms
from .models import SituatieScolara
from django.forms import ModelForm

class AdaugareNoteForm(ModelForm):
    class Meta:
        model = SituatieScolara
        fields = ('nota', 'materia')
