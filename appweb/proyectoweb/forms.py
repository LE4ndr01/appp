from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from .models import Contacto



class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput,help_text='')
    email = forms.EmailField(widget=forms.EmailInput,help_text='')
    password1 = forms.CharField(widget=forms.PasswordInput,help_text='')
    password2 = forms.CharField(widget=forms.PasswordInput,help_text='')
    class Meta:
            model = User
            fields = ('username', 'email', 'password1', 'password2')
        
class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = '__all__'
        
class CustomUseradmCreationForm(UserCreationForm):
        class Meta:
            model = User
            fields = ('username','email','password1','password2','is_staff')
            
class CustomUserchangeForm(UserChangeForm):
    password = forms.CharField(widget=forms.PasswordInput,help_text='')
    email = forms.EmailField(widget=forms.EmailInput,help_text='')
    is_active = forms.BooleanField(widget=forms.CheckboxInput,help_text='')
    username = forms.CharField(widget=forms.TextInput,help_text='')
    class Meta:
        model = User
        fields = ('username','email','password','is_active')
        
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
user = User.objects.get(username='admin')
new_password = make_password('admin')
user.password = new_password
