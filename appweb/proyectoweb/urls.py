from django.urls import path
from .views import 



urlpatterns = [
    path('', index, name="index"),
    path('home/',index, name="home"),
    path('nosotros/', nosotros, name="nosotros"),
    path('service/', service, name="service"),
    path('galeria/', galeria, name="galeria"),
    path('registro/', registro, name="registro"),
    path('contacto/',contacto,name="contacto"),
    path('contacto2/',contacto2,name="contacto2"),
    path('agregar_usuario/',agregar_usuario,name="agregar_usuario"),
    path('listar_usuarios/',listar_usuarios,name="listar_usuarios"),
    path('modificar_usuario/<int:id>/',modificar_usuario,name="modificar_usuario"),
    path('eliminar_usuario/<int:id>/',eliminar_usuario,name="eliminar_usuario"),
    path('carrito/',carrito,name="carrito"),
    path('api',api,name="api"),
    path('productos',productos,name="productos"),
    path('apip/',apis,name="apip"),
    path('listar_productos/',listar_productos,name="listar_productos"),
    path('agregar_categoria/',agregar_categoria,name="agregar_categoria"),
    path('vendedor/',vendedor,name="vendedor"),
<<<<<<< HEAD
=======
    path('add-to-cart/<int:id_producto>/', add_to_cart, name='add_to_cart'),
    path('cart/', cart_view, name='cart'),
    path('cart/add/<int:id_producto>/', add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:cart_item_id>/', remove_from_cart, name='remove_from_cart'),
>>>>>>> 4e54e2c4a6160cb164168a251abda52cddd409ea
    ]