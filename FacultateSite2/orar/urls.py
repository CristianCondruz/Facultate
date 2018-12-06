from . import views
from django.urls import path, include
app_name = 'orar'

urlpatterns = [
    path('creare_orar/',views.CreareOrarView,name='creare_orar'),
    # path('adaugare_note/',views.adaugare_note,name='adaugare_note'),
    # path('selectie_materii/',views.SelectieMateriiView,name='selectie_materii'),
    # path('creare_grupe/',views.CreareGrupeView,name='creare_grupe')
]
