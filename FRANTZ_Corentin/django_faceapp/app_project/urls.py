from django.urls import path, include
from app_project import views
from django.views.generic.base import TemplateView
from django.contrib.auth.views import LogoutView
from django.conf import settings

urlpatterns = [
    path('', TemplateView.as_view(template_name='app_project/main.html'), name="main"),
    path('signup/', views.signup, name='signup'),
    path('account/', include('django.contrib.auth.urls')),
    path('success/', views.success, name='success'),
]
