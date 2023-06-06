from django.contrib import admin
from .models import Producto,Contacto

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'descripcion', 'imagen')

# Register your models here.

admin.site.register(Producto, ProductoAdmin)
admin.site.register(Contacto)

