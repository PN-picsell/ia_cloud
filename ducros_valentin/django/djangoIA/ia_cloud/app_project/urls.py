from django.urls import path, include
from app_project import views

urlpatterns = [
    path('project/', views.home, name='home'),
    path('project/hello_world', views.hello_world, name="hello_world"),
    path('project/signup', views.signup, name='signup'),
    path('project/logout_view', views.logout_view, name='logout_view'),
    path('project/signin', views.signin, name='signin')
]