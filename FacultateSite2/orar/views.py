from django.shortcuts import render
from .forms import CreareOrarForm
from.models import Orar
# Create your views here.
def CreareOrarView(request):

    if request.method == 'POST':
        creare_orar_form = CreareOrarForm(request.POST)
        if creare_orar_form.is_valid():
            ziua_saptamanala = creare_orar_form.cleaned_data.get('ziua_saptamanala')
            locatia = creare_orar_form.cleaned_data.get('locatia')
            materia = creare_orar_form.cleaned_data.get('materia')
            anul = creare_orar_form.cleaned_data.get('anul')
            tip = creare_orar_form.cleaned_data.get('tip')
            intervalul_orar = creare_orar_form.cleaned_data.get('intervalul_orar')
            o1 = Orar(ziua_saptamanala=ziua_saptamanala,locatia=locatia,materia=materia,anul=anul,tip=tip,intervalul_orar=intervalul_orar)
            o1.save()
    else:
        creare_orar_form = CreareOrarForm()

    return render(request, 'creare_orar.html',{
			'CreareOrarForm': CreareOrarForm,
		})
