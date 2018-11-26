from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import AdaugareNoteForm, SelectieMateriiForm, CreareGrupeForm, AdaugareNoteForm, MateriiGrupaForm, StudentInfoForm
from django.http import HttpResponseRedirect
from accounts.models import ProfesorMateria
from .models import MateriiGrupa, Grupa
from accounts.models import Profesor


# Create your views here.

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
    if request.method == 'POST':
        creare_grupe_form = CreareGrupeForm(request.POST)
        if creare_grupe_form.is_valid():
            g1 = Grupa(numarul=creare_grupe_form.cleaned_data.get('numarul'), seria=creare_grupe_form.cleaned_data.get('seria'))
            g1.save()
            for materia in creare_grupe_form.cleaned_data.get('materia'):
                mg1 = MateriiGrupa(materie=materia, grupa=g1)
                mg1.save()

    else:
        creare_grupe_form = CreareGrupeForm()
    return render(request, 'creare_grupe.html',{
			'creare_grupe_form': creare_grupe_form,
		})

def adaugare_note(request):
    current_profesor = Profesor.objects.get(pk = request.user.profesor.id)
    print(current_profesor.objects.filter(profesorMateria))
    if request.method == 'POST':
        adaugare_note_form = AdaugareNoteForm(request.POST)
        materii_grupe_form = MateriiGrupaForm(request.POST)
        student_form = StudentInfoForm(request.POST)
    else:
        adaugare_note_form = AdaugareNoteForm()
        materii_grupe_form = MateriiGrupaForm()
        student_form = StudentInfoForm()
    return render(request, 'adaugare_note.html',{
			'adaugare_note_form': adaugare_note_form,
            'materii_grupe_form': materii_grupe_form,
            'student_form': student_form
		})
