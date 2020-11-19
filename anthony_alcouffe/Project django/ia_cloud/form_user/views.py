from django.shortcuts import render, redirect
from django.http import HttpResponse
from form_user.forms import SignUpForm, LoginForm
from form_user.models import Profil
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout

def logout_view(request):
    logout(request)
    return redirect('home')

def home(request):
    return render(request, 'form_user/home.html')

# FIXME probleme du champ password qui s'affiche seulement apres avoir appuyé sur login
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return render(request, 'form_user/login.html', {'form': form,})
        else:
            return render(request, 'form_user/login.html', {'form': form,})
    else:
        form = SignUpForm(request.POST)
        return render(request, 'form_user/login.html', {'form': form,})


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            firstname = form.cleaned_data.get('firstname')
            lastname = form.cleaned_data.get('lastname')
            location = form.cleaned_data.get('location')
            profil = Profil.objects.create(user=User.objects.create_user(username, email, password), firstname=firstname, lastname=lastname, location=location )
            profil.save()
            profil.user.is_active = True
            login(request, profil.user, backend='django.contrib.auth.backend.ModelBackend')
            return redirect('login')
        else:
            return render(request, 'form_user/register.html', {'form': form,})
    else:
        form = SignUpForm(request.POST)
        return render(request, 'form_user/register.html', {'form': form,})



# Create your views here.
