import mercadopago
<<<<<<< HEAD



=======
from zeep import Client
from .producto import *


class Controller:
    wsdl = 'http://localhost:8080/Webaires/wsAC?wsdl'
    cliente = Client(wsdl)

    def buscarproducto(self):
        productos = self.cliente.service.ListaAC()
        lista_productos = []
        for p in productos:
            producto = Producto(
                id_producto=p['codigo'],
                nombre=p['nombre'],
                marca=p['marca'],
                descripcion='',
                precio=p['precio'],
                stock=p['stock']
            )
            lista_productos.append(producto)
        return lista_productos

'''
>>>>>>> 877f62365871c31cf82c1bd6c513737e054b58d6
def pagar(self):
sdk = mercadopago.SDK("TEST-897243312298306-061023-3c50ea005623944e7672975229c97897-1381947166")


#vendedor
#{"id":123456789, "nickname":TESTT63111, "password":iBr9ihiqlT, "site_estatus":"active","email:"test_user1381493535@testuser.com"}
preference_data = {
    "items": [
        {
            "producto":"Aire Acondicionado 1",
            "id":1,
            "description": "AACC1",
            "quantity":2,
            "unit_price": 180000 
        }
        {
            "producto":"Aire Acondicionado 2",
            "id":2,
            "description": "AACC2",
            "quantity":1,
            "unit_price": 220000 
        }
    ]
    "back_urls": { 
        "success":"http://127.0.0.1:8000/",
        "failure":"http://127.0.0.1:8000/",
        "pending":"http://127.0.0.1:8000/"
    }
    "auto_return": "approved"
}

preference_responce = sdk.preference().create(preference_data)
#preference = preference_response["responce"]
return preference_responce  
'''

