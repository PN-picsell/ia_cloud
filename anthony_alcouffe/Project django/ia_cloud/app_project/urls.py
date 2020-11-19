from app_project import views
from django.urls import path, include

urlpatterns = [
    #path('project/hello_world/', views.hello_world, name='hello_world' ),
    path('project/hello_world/<id>', views.hello_world, name='hello_world' ),
]
