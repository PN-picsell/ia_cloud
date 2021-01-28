from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import SignUpForm, ImageForm
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.contrib.auth import authenticate
from django.views.generic import DetailView
from .neuronalNetwork import *
from .awsApi import *


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

def image_view(request): 
  
    if request.method == 'POST': 
        url = request.POST['userUrl']
        now = WordDetection(url)
        html = "<img src=\""+url+"\" alt=\"Italian Trulli\">" + now
        return HttpResponse(html)
    else: 
        return render(request, 'app_project/uploadImage.html') 
  
  
def successUpload(request): 
    return HttpResponse('successfully uploaded') 

def sendUrl(request):
    if request.method == 'POST': 
       
        url = request.POST['userUrl']
        now = WordDetection(url)
        html = "<img src=\""+url+"\" alt=\"Italian Trulli\">" +"</br>"+ now
        return HttpResponse(html)


class UserImage(TemplateView):
    form = ImageForm
    template_name = 'uploadImage.html'

    def post(self, request, *args, **kwargs):
        form = ImageForm(request.POST, request.FILES)
        if form:
            form.save()
            return HttpResponseRedirect(reverse_lazy('successImage', kwargs.get('pk')))
        context = self.get_context_data(form=form)
        return self.render_to_response(context)     

    def get(self, request, *args):
        return self.post(request, *args)
    


def EmpImageDisplay(request): 
    if request.method == 'POST': 
        now = "c"
        url = request.POST['userUrl']
            
        html = "<img src=\""+url+"\" alt=\"Italian Trulli\">" + now
        return HttpResponse(html) 
    else: 
        return render(request, 'app_project/AWSImage.html') 
        

