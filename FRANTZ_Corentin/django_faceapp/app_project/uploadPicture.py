from django import forms 
from .models import Image

class EmployeeForm(forms.ModelForm): 
    class Meta: 
        model = Image 
        fields = [ 'image']