from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import AdaugareNoteForm, SelectieMateriiForm, CreareGrupeForm
from django.http import HttpResponseRedirect
from accounts.models import ProfesorMateria
from .models import MateriiGrupa


# Create your views here.

class AdaugareNoteView(FormView):
    template_name = 'adaugare_note.html'
    form_class = AdaugareNoteForm
    success_url = 'adaugare_note.html'

def SelectieMateriiView(request):

    if request.method == 'POST':
        selectie_materii_form = SelectieMateriiForm(request.POST)

        if selectie_materii_form.is_valid():
            current_profesor = request.user.profesor
            for materie in selectie_materii_form.cleaned_data.get('materia'):
                p1 = ProfesorMateria(profesor=current_profesor, materia = materie)
                p1.save()
    else:
        selectie_materii_form = SelectieMateriiForm()
    return render(request, 'selectie_materii.html',{
			'selectie_materii_form': selectie_materii_form,
		})

def CreareGrupeView(request):
    if request.method = 'POST':
        creare_grupe_form = CreareGrupeForm(request.POST)
        if creare_grupe_form.is_valid():
            g1 = Grupa(numarul=creare_grupe_form.get('numarul'), seria=creare_grupe_form.get('seria'))
            g1.save()
            for materia in creare_grupe_form.get('materia'):
                mg1 = MateriiGrupa(materie=materia, grupa=g1)
                mg1.save()

    else:
        creare_grupe_form = CreareGrupeForm()
    return render(request, 'creare_grupe.html',{
			'creare_grupe_form': creare_grupe_form,
		})
