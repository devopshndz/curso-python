# busquedad e elementos de un listado con el metodo index()
mascotas = ["perro", "gato", "pollo", "gusano"]

if "gato" in mascotas: # si el elemento existe
    print(mascotas.index("gato")) # al imprimir, develve la posición en donde se encuentra el elemento gato+

# que pasa si hay un elemento repetido:
mascotas = ["perro", "gato", "pollo", "gusano", "gato"]

print(mascotas.count("gato"))
if "gato" in mascotas: # si el elemento existe
    print(mascotas.index("gato"))