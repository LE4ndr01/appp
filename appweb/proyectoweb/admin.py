from django.contrib import admin
from .models import Articulo,Contacto

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'descripcion', 'imagen')

# Register your models here.

admin.site.register(Articulo, ProductoAdmin)
admin.site.register(Contacto)

