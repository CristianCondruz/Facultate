from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import AdaugareNoteForm

# Create your views here.

class AdaugareNoteView(FormView):
    template_name = 'adaugare_note.html'
    form_class = AdaugareNoteForm
    success_url = 'adaugare_note.html'

    
