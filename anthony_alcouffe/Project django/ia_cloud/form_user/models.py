from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Profil(models.Model):
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    create_at = models.DateField(auto_now_add=True, editable=False)
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    location = models.CharField(max_length=200)

    