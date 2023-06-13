from django.db import models

# Create your models here.
class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    
    def __str__(self):
        return self(self.id_categoria)
    

class Articulo(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    imagen = models.ImageField(upload_to="img", null=True)
    Categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id_producto)


opciones_consulta = [
    [0,"Consulta"],
    [1,"Reclamo"],
    [2,"sugerencia"],
]



class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    tipo_consulta = models.IntegerField(choices=opciones_consulta, default=0)
    mensage = models.TextField()
    def __str__(self):
        return self.nombre
