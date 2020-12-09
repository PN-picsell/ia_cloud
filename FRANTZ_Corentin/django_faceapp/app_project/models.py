from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=50, unique= False, null=False)
    lastname = models.CharField(max_length=50, unique= False, null=False)
    location = models.CharField(max_length=50, unique= False, null=False)
    creation_date = models.DateTimeField(auto_now_add=True)
    