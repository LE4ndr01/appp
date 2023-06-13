from django.contrib import admin
from .models import Articulo, Contacto, Categoria

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'descripcion', 'imagen')
    
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id_categoria','nombre',)

admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Articulo, ProductoAdmin)
admin.site.register(Contacto)