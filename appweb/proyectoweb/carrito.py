from django.contrib import messages
class Carrito:
    def __init__(self,request):
        self.request = request
        self.session = request.session
        carrito = self.session('carrito')
        if not carrito:
            self.session["carrito"] = {}
            self.carrito = self.session["carrito"]
        else:
            self.carrito = carrito
            

################################
#  Añadir producto a carrito   #
################################

def add_carrito(self,Articulo):
    if str(Articulo.id) not in self.carrito.keys():
        self.carrito[Articulo.id] = {
            "producto_id":Articulo.id,
            "name":Articulo.name,
            "cantidad" : 1,
            "precio" :  Articulo.precio,
            "imagen" : Articulo.imagen.url,
        }
        
    else:
        self.carrito[Articulo.id]["cantidad"] =+ 1
        self.carrito[Articulo.id]["precio"] =+ Articulo.precio
    self.save()
    
################################
#  Guardar producto de carrito #
################################

def save(self):
    self.session["carrito"] = self.carrito
    self.session.modified = True
    
#################################
#  Eliminar producto de carrito #
#################################

def eliminar(self,Articulo):
    Articulo_id = str(Articulo.id)
    if Articulo_id in self.carrito:
        del self.carrito[Articulo_id]
        self.save()
        messages.success(self.request,'Producto eliminado de carrito')

#################################
# disminuir producto de carrito #
#################################

def restar(self,Articulo):
    if str(Articulo.id) in self.carrito.keys():
        self.carrito[Articulo.id]["cantidad"] =- 1
        self.carrito[Articulo.id]["precio"] =- Articulo.precio
        if self.carrito[Articulo.id]["cantidad"] <= 0: self.eliminar(Articulo)
        self.save()
        

################################
#        limpiar carrito       #
################################

def limpiar(self):
    self.session["carrito"] = {}
    self.session.modified = True
            
    
        
        
    
                