from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth import authenticate


# Create your views here
def main(request):
    return render(request, 'app_project/main.html', locals())

def success(request):
    return render(request, 'app_project/success.html', locals())

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            location = form.cleaned_data.get('location')
            user = User.objects.create_user(username, email, password)
            user.is_active = True
            user.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('success')
        else:
            return render(request, 'app_project/registration.html', {
                'form': form,
            })
    else:
        form = SignUpForm()
        return render(request, 'app_project/registration.html', {
             'form': form,
        })


