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
        
class CustomUseradmCreationForm(UserCreationForm):
        class Meta:
            model = User
            fields = ('username','email','password1','password2','is_staff')