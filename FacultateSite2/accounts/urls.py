from django.urls import path, reverse_lazy, re_path, include
from django.contrib.auth import views as auth_views
from . import views


app_name = 'accounts'

urlpatterns = [
    path('signup_professor', views.profesor_view,name='signup_professor'),
    path('signup_student', views.student_view,name='signup_student'),
    #path('login', auth_views.LoginView.as_view(template_name='accounts/login.html'),name='login'),
    path('login/', views.user_login ,name='login'),
    path('logout/',views.user_logout ,name='logout'),
    path('sign_up/',views.SignUp.as_view(),name='sign_up'),
    re_path('date_personale_student/(?P<pk>\d+)/(?P<name>\w+)/$',views.DatePersonaleStudentView.as_view(),name='date_personale_student'),
    re_path('date_personale_profesor/(?P<pk>\d+)/(?P<name>\w+)/$',views.DatePersonaleProfesorView.as_view(),name='date_personale_profesor'),
]
