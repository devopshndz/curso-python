mascotas = ["Wolfgang", "Pelusa", "Pulga", "Copito"]
print(mascotas[0]) # indice de ubicacion de elementos de listas.
mascotas[0]= "Bicho"
print(mascotas) # cambiamos el primer elemento por Bicho
print(mascotas[2:]) # desde donde queremos ver:hasta donde queremos ver
print(mascotas[-1])
print(mascotas[::2]) # Elementos pares de un listado

numeros = list(range(21))
print(numeros[1::2])
print(numeros[::2])