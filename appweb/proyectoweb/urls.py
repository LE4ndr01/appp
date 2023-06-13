from django.urls import path
from .views import *



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
    path('modificar_usuario/<int:id>/',modificar_usuario,name="modificar_usuario"),
    path('eliminar_usuario/<int:id>/',eliminar_usuario,name="eliminar_usuario"),
    path('carrito/',carrito,name="carrito"),
    path('api',api,name="api"),
    path('productos',productos,name="productos"),
    path('apip/',apis,name="apip"),
    path('listar_productos/',listar_productos,name="listar_productos"),
    ]