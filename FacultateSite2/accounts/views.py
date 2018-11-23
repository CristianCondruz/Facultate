from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views import generic

from .forms import CustomUserCreationForm, StudentForm, ProfesorForm
from .models import CustomUser, Student, Profesor
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.contrib.auth.backends import ModelBackend

class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('accounts:login')
    template_name = 'accounts/signup.html'

def student_view(request):
    registered = False

    if request.method == 'POST':
        user_form = CustomUserCreationForm(request.POST)
        student_form = StudentForm(request.POST)

        if user_form.is_valid() and student_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(request.POST["password1"])
            user.is_student = True
            user.save()
            user.student.grupa = student_form.cleaned_data.get('grupa')
            user.student.an = student_form.cleaned_data.get('an')
            user.student.nume = student_form.cleaned_data.get('nume')
            user.student.prenume = student_form.cleaned_data.get('prenume')
            user.student.data_nastere = student_form.cleaned_data.get('data_nastere')
            user.student.adresa_domiciliu = student_form.cleaned_data.get('adresa_domiciliu')
            user.student.cnp = student_form.cleaned_data.get('cnp')
            user.student.facebook_site = student_form.cleaned_data.get('facebook_site')
            user.student.linkedin_site = student_form.cleaned_data.get('linkedin_site')
            user.student.grupa = student_form.cleaned_data.get('grupa')
            if 'profile_pic' in request.FILES:
                user.student.profile_pic = request.FILES['profile_pic']
            user.student.save()
            registered = True
    else:
        user_form = CustomUserCreationForm()
        student_form = StudentForm()


    return render(request, 'accounts/signup_student.html',{
			'user_form': user_form,
			'student_form': student_form,
            'registered': registered
		})

#View function for Professor registration
def profesor_view(request):
    registered = False

    if request.method == 'POST':
        user_form = CustomUserCreationForm(request.POST)
        profesor_form = ProfesorForm(request.POST)

        if user_form.is_valid() and profesor_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(request.POST["password1"])
            user.is_student = False
            user.save()
            user.profesor.nume = profesor_form.cleaned_data.get('nume')
            user.profesor.prenume = profesor_form.cleaned_data.get('prenume')
            user.profesor.grad = profesor_form.cleaned_data.get('grad')
            user.profesor.facebook_site = profesor_form.cleaned_data.get('facebook_site')
            user.profesor.linkedin_site = profesor_form.cleaned_data.get('linkedin_site')
            user.profesor.research_gate_profile = profesor_form.cleaned_data.get('research_gate_profile')
            if 'profile_pic' in request.FILES:
                user.profesor.profile_pic = request.FILES['profile_pic']
            user.profesor.save()
            registered = True
    else:
        user_form = CustomUserCreationForm()
        profesor_form = ProfesorForm()


    return render(request, 'accounts/signup_professor.html',{
			'user_form': user_form,
			'profesor_form': profesor_form,
            'registered': registered
		})

def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        print(password)
        UserModel = get_user_model()
        user = UserModel._default_manager.get_by_natural_key(username)
        mb = ModelBackend()
        print(mb.user_can_authenticate(user = user))
        print(user.check_password(password))
        user = authenticate(username=username,password=password,request=request)
        print(user.is_student)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('home'))
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            print("Someone tried to login and failed")
            return HttpResponse("Invalid login details")
    else:
        return render(request,'accounts/login.html',{})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

class DatePersonaleStudentView(generic.DetailView):
    model = Student
    template_name='accounts/date_personale.html'

class DatePersonaleProfesorView(generic.DetailView):
    model = Profesor
    template_name='accounts/date_personale.html'
