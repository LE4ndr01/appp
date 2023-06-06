from django.shortcuts import render,redirect
from django.contrib.auth import login as auth_login,authenticate
from django.contrib import messages
from .forms import CustomUserCreationForm,ContactoForm,UsuarioForm
from django.http import HttpResponse
from .models import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# Create your views here.
TEMPLATE_DIRS =(
    'os.path.join(BASE_DIR,"templates"),'
    
)

def index(request):
    return render(request,"index.html")

def nosotros(request):
    return render(request,"nosotros.html")

def service(request):
    return render(request,"service.html")

def galeria(request):
    productos= Producto.objects.all()
    datos= {
        'lista': productos,
    }
    return render(request,"galeria.html",datos)

def login(request):
    return render(request,"registration/login.html")

def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }
    
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            usuario = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            if usuario is not None:
                auth_login(request, usuario)
                messages.success(request, 'Usuario creado exitosamente')
                return redirect(to="index")
            else:
                messages.error(request, 'No se pudo autenticar al usuario')
        
        data['form'] = formulario
    
    return render(request, "Registration/formulario_registro.html", data)

@login_required()
def contacto(request):
    data = {
        'form': ContactoForm()
    }
    if request.method == 'POST':
        formulario = ContactoForm(data = request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Mensaje enviado exitosamente')
    
    return render(request,"contact.html",data)

#############################################
#   Agregar  Listar  Modificar  Eliminar    #
#############################################

### Agregar usuario ###
@login_required()
def agregar_usuario(request):
    
    data = {
        'form': UsuarioForm()
    }
    if request.method == 'POST':
        formulario = UsuarioForm(data = request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Usuario creado exitosamente')
        else:
            data['form'] = formulario
        
    
    return render(request,"Crud/agregar.html",data)

### Agregar usuario ###

def listar_usuarios(request):
    usuarios = User.objects.all()
    return render(request,"Crud/listar.html", {'usuarios':usuarios})