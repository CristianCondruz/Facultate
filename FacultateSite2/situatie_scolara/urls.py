from django.urls import path, reverse_lazy, re_path, include
from django.contrib.auth import views as auth_views
from . import views


app_name = 'situatie_scolara'

urlpatterns = [
    path('adaugare_note/',views.AdaugareNoteView.as_view(),name='adaugare_note')

]
