# kwargs arguments, forma de empaquetar todos nuestros parametros en solo 1 parametro.

def get_product(**datos): # ** para que sea kwargs
    print(datos)

get_product(id="id") # cada vez que esté usando kwargs, debo de agregar el nombre del parametro, le podemos pasar todos los argumentos que queramos pero con esta forma
# se imprime un diccionario: {'id': 'id'}
get_product(name="iphone", desc="Esto es un celular")

### forma para solo escoger cierta cantidad de datos y no todos []
def get_producto(**datos):
    print(datos["id"], datos["name"]) # se especifica cuales son los datos a ver antecedido por el nombre del parametro datos

get_producto(id="id",
            name="Xiaomi",
            desc="best phone")
