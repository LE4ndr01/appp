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

def add_carrito(self,producto):
    if str(producto.id) not in self.carrito.keys():
        self.carrito[producto.id] = {
            "producto_id":producto.id,
            "name":producto.name,
            "cantidad" : 1,
            "precio" :  producto.precio,
            "imagen" : producto.imagen.url,
        }
        
    else:
        self.carrito[producto.id]["cantidad"] =+ 1
        self.carrito[producto.id]["precio"] =+ producto.precio
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

def eliminar(self,producto):
    producto_id = str(producto.id)
    if producto_id in self.carrito:
        del self.carrito[producto_id]
        self.save()
        messages.success(self.request,'Producto eliminado de carrito')

#################################
# disminuir producto de carrito #
#################################

def restar(self,producto):
    if str(producto.id) in self.carrito.keys():
        self.carrito[producto.id]["cantidad"] =- 1
        self.carrito[producto.id]["precio"] =- producto.precio
        if self.carrito[producto.id]["cantidad"] <= 0: self.eliminar(producto)
        self.save()
        

################################
#        limpiar carrito       #
################################

def limpiar(self):
    self.session["carrito"] = {}
    self.session.modified = True
            
    
        
        
    
                