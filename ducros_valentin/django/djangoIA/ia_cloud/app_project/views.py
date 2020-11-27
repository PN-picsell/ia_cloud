from django.shortcuts import render, redirect
from django.http import HttpResponse
from app_project.models import Profile
from app_project.forms import SignUpForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/signin')
def hello_world(request):
    print('hello_world')
    user = request.user
    return render(request, 'app_project/hello_world.html',locals())

def home(request):
    print('home')
    user = request.user
    if user.is_authenticated == True:
        return render(request, 'app_project/home.html', {
            'user': user
        })
    else :
        return render(request, 'app_project/signin.html')

def signup(request):
    print('signup')
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = User.objects.create_user(username,email,password)
            user.is_active = True
            user.save()
            profile = Profile(user=user)
            profile.save()
            login(request,user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('hello_world')
        else :
            return render(request, 'app_project/signup.html', {
                'form': form,
            })
    else:
        form = SignUpForm()
        return render(request, 'app_project/signup.html', {
            'form': form,
        })

def signin(request):
    print('signin')
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request,user, backend='django.contrib.auth.backends.ModelBackend')
        return redirect('home')
    else:
        print('faild authenticate')
        return render(request, 'app_project/signin.html', {
            'errors': "errorLogin"
        })

def logout_view(request):
    print('logout')
    logout(request)
    return redirect('home')