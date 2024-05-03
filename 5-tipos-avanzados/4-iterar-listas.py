# iterar elementos de un listado
mascotas = ["perro", "gato", "pollo", "gusano"]
for mascota in mascotas:
    print(mascota)


for indice, mascota in enumerate(mascotas): # esto devuelve una tupla [(),()]
    print(indice, mascota)
