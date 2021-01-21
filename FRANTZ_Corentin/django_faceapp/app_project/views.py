from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import SignUpForm, Image
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.contrib.auth import authenticate
from django.views.generic import DetailView


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


class UserImage(TemplateView):
    form = Image
    template_name = 'uploadImage.html'

    def post(self, request, *args, **kwargs):
        form = Image(request.POST, request.FILES)
        if form:
            form.save()
            return HttpResponseRedirect(reverse_lazy('successImage', kwargs.get('pk')))
        context = self.get_context_data(form=form)
        return self.render_to_response(context)     

    def get(self, request, *args):
        return self.post(request, *args)
    

class EmpImageDisplay(DetailView):
    model = Image
    template_name = 'displayImage.html'
    context_object_name = 'use'