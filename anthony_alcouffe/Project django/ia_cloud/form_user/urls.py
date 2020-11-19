from . import views
from django.urls import path, include

urlpatterns = [
    path('login/', views.login_view, name='login' ),
    path('register/', views.register, name='register' ),
    path('logout/', views.logout_view, name='logout'),
    path('', views.home, name='home' ),
]
