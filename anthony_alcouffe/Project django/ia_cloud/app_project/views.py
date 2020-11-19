from django.shortcuts import render
from django.http import HttpResponse

def hello_world(request, id):
    return render(request, 'app_project/hello_world.html', locals())

# Create your views here.
