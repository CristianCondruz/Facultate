from django import forms
from situatie_scolara.models import Grupa, Materii
from .models import Locatii, Orar

class CreareOrarForm(forms.ModelForm):

    class Meta:
        model = Orar
        fields = ('ziua_saptamanala','locatia','materia','anul','tip', 'intervalul_orar')

class MateriaForm(forms.ModelForm):

    class Meta:
        model = Materii
        fields = ('nume',)

class LocatiaForm(forms.ModelForm):

    class Meta:
        model = Locatii
        fields = ('corpul', 'sala')
