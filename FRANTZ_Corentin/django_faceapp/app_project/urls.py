from django.urls import path, include
from app_project import views
from django.views.generic.base import TemplateView
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', TemplateView.as_view(template_name='app_project/main.html'), name="main"),
    path('signup/', views.signup, name='signup'),
    path('account/', include('django.contrib.auth.urls')),
    path('success/', views.success, name='success'),
    path('successImage/', views.success, name='successImage'),
    path('upload/', views.UserImage.post, name='uploadImage'),
    path('awsRekognition/', views.EmpImageDisplay, name='detectImageAws'),
]

if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)