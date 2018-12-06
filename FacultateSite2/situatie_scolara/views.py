from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import AdaugareNoteForm, SelectieMateriiForm, CreareGrupeForm, AdaugareNoteForm, MateriiGrupaForm, StudentInfoForm
from django.http import HttpResponseRedirect
from accounts.models import ProfesorMateria, Student
from .models import MateriiGrupa, Grupa, SituatieScolara
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
    e = ProfesorMateria.objects.all()
    #print(current_profesor.materia_profesor.all().order_by('materia').all()[0].all())
    if request.method == 'POST':
        adaugare_note_form = AdaugareNoteForm(request.POST)
        materii_grupe_form = MateriiGrupaForm(request.POST)
        student_form = StudentInfoForm(request.POST)
        if adaugare_note_form.is_valid() and student_form.is_valid():
            if adaugare_note_form.cleaned_data.get('nota') > 5:
                ss = SituatieScolara(nota=adaugare_note_form.cleaned_data.get('nota'),
                        materia=adaugare_note_form.cleaned_data.get('materia'),admis=True)
            else:
                ss = SituatieScolara(nota=adaugare_note_form.cleaned_data.get('nota'),
                        materia=adaugare_note_form.cleaned_data.get('materia'),admis=False)
            ss.save()
            print(ss)
            student_notat = Student.objects.get(nume=student_form.cleaned_data.get('nume'),
                prenume=student_form.cleaned_data.get('prenume'))
            student_notat.situatie_scolara = ss
            student_notat.save()
    else:
        adaugare_note_form = AdaugareNoteForm()
        materii_grupe_form = MateriiGrupaForm()
        student_form = StudentInfoForm()
    return render(request, 'adaugare_note.html',{
			'adaugare_note_form': adaugare_note_form,
            'materii_grupe_form': materii_grupe_form,
            'student_form': student_form
		})
def vizualizare_situatie_scolara(request):
    current_student = Student.objects.get(pk = request.user.student.id)
    situatie_scolara = current_student.situatie_scolara
    print(situatie_scolara)
    return render(request, 'vizualizare_situatie_scolara.html',{
    'nota' : [situatie_scolara.nota],
    'materia' : [situatie_scolara.materia],
    'admis' : [situatie_scolara.admis],
    'data_notarii' : [situatie_scolara.data_notarii],
    })
