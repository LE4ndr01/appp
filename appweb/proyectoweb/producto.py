class Producto:
    id_producto =0
    nombre = ""
    marca = ""  
    descripcion = ""
    precio = ""
    stock = ""
    
    def __init__(self,id_producto,nombre,marca,descripcion,precio,stock):
        self.id_producto = id_producto
        self.nombre = nombre
        self.marca = marca
        self.descripcion = descripcion
        self.precio = precio
        self.stock = stock
        
    def prodducroArr(self):
        return {
            'codigo': self.id_producto,
            'nombre': self.nombre,
            'marca': self.marca,
            'descripcion': self.descripcion,
            'precio': self.precio,
            'stock': self.stock
        }
    def __str__(self):
        return 'codigo:'+self.id_producto+'nombre:'+self.nombre+'descripción:'+self.descripcion+'marca:'+self.marca+'precio:'+self.precio+'stock:'+self.stock
    
                