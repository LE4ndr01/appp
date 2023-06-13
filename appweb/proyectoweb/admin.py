from django.contrib import admin
from .models import Articulo, Contacto, Categoria

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'descripcion', 'imagen')
    


admin.site.register(Categoria)
admin.site.register(Articulo, ProductoAdmin)
admin.site.register(Contacto)