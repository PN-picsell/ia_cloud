from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    username = forms.CharField(label="", max_length=100,
    widget=forms.TextInput(attrs={
        "placeholder": "Username",
        "class": "form-control",
        "id": "username"
    }))
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
    location = forms.CharField(
        label='',
        max_length=255,
        required=True,
        widget=forms.TextInput(attrs={
        "placeholder": "Location",
        "class": "form-control",
        "id": "location"
    })
    )

    password1 = forms.CharField(
        label='',
        max_length=100,
        min_length=8,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        )
    )

    password2 = forms.CharField(
            label='',
            max_length=100,
            min_length=8,
            required=True,
            widget=forms.PasswordInput(
                attrs={
                    "placeholder": "Confirm Password",
                    "class": "form-control"
                }
            )
        )

    class SignInForm(User):
        username = forms.CharField(label="", max_length=100,
        widget=forms.TextInput(attrs={
            "placeholder": "Username",
            "class": "form-control",
            "id": "username"
        }))

        password = forms.CharField(
            label='',
            max_length=100,
            min_length=8,
            required=True,
            widget=forms.PasswordInput(
                attrs={
                    "placeholder": "Password",
                    "class": "form-control",
                    "id": "password"
                }
            )
        )


    class Meta:
        model = User
        fields = ('email', 'password1', 'password2', 'location')
