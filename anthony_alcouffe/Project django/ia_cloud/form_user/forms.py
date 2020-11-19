from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from form_user.models import Profil
    

class SignUpForm(UserCreationForm):
    username = forms.CharField(label="", required=True, max_length=100, widget=forms.TextInput(attrs={"placeholder":"Username",
                                                                                                    "class": "form-control",
                                                                                                    "id": "username"
                                                                                                    }
                                                                                )
                              )
        
    password1 = forms.CharField(
        label='',
        max_length=90,
        min_length=8,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "paceholder": "password",
                "class": "form-control"
            }
        )
    )

    password2 = forms.CharField(
        label='',
        max_length=90,
        min_length=8,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "paceholder": "Confirm Password",
                "class": "form-control"
            }
        )
    )

    email = forms.EmailField(
        label='',
        max_length=255,
        required=True,
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email",
                "class": "form-control"
            }
        )
    )

    firstname = forms.CharField(
        label='',
        max_length=255,
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": "firstname",
                "class": "form-control"
            }
        )
    )

    lastname = forms.CharField(
        label='',
        max_length=255,
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": "lastname",
                "class": "form-control"
            }
        )
    )

    location = forms.CharField(
        label='',
        max_length=255,
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": "location",
                "class": "form-control"
            }
        )
    )

    class Meta:
        model = User
        profil = Profil
        fields = ('username', 'email', 'password1', 'password2', 'firstname', 'lastname', 'location')

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={"placeholder":"Username",
                                                                                        "class": "form-control",
                                                                                        "id": "username"
                                                                                                    }
                                                                                )
                              )
        
    password = forms.CharField(
        label='',
        max_length=90,
        min_length=8,
        widget=forms.PasswordInput(
            attrs={
                "paceholder": "password",
                "class": "form-control"
            }
        )
    )

    class Meta:
        model = User
        profil = Profil
        fields = ('username', 'password')