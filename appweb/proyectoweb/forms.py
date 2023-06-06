from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Contacto



class CustomUserCreationForm(UserCreationForm):
        class Meta:
            model = User
            fields = ('username','email','password1','password2')
        
class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = '__all__'
        
class UsuarioForm(forms.Form):
    username = forms.CharField(label='Usuario')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput)
    is_staff = forms.BooleanField(label='es staff')
