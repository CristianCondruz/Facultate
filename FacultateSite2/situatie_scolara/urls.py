from django.urls import path, reverse_lazy, re_path, include
from django.contrib.auth import views as auth_views
from . import views


app_name = 'situatie_scolara'

urlpatterns = [
    path('vizualizare_situatie_scolara/',views.vizualizare_situatie_scolara,name='vizualizare_situatie_scolara'),
    path('adaugare_note/',views.adaugare_note,name='adaugare_note'),
    path('selectie_materii/',views.SelectieMateriiView,name='selectie_materii'),
    path('creare_grupe/',views.CreareGrupeView,name='creare_grupe')
]
