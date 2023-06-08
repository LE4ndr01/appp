from django.urls import path
from .views import index, nosotros, service, galeria, registro, contacto,agregar_usuario,listar_usuarios,carrito



urlpatterns = [
    path('', index, name="index"),
    path('home/',index, name="home"),
    path('nosotros/', nosotros, name="nosotros"),
    path('service/', service, name="service"),
    path('galeria/', galeria, name="galeria"),
    path('registro/', registro, name="registro"),
    path('contacto/',contacto,name="contacto"),
    path('agregar_usuario/',agregar_usuario,name="agregar_usuario"),
    path('listar_usuarios/',listar_usuarios,name="listar_usuarios"),
    path('carrito/',carrito,name="carrito"),
    ]