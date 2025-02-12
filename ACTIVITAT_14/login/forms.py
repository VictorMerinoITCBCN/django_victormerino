from django import forms
from .models import User

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("name", "last_name", "email", "password")

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("email", "password")
    email = forms.CharField(label="Email")
    password = forms.CharField(label="Password", widget=forms.PasswordInput())