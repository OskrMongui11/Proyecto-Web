from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Proceso, TipoProceso, Cliente

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class ProcesoForm(forms.ModelForm):
    class Meta:
        model = Proceso
        fields = ['doc_online', 'doc_fisico', 'cliente', 'tipo_proceso']