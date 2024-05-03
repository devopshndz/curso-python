mascotas = ["perro", 
            "gato", 
            "pollo", 
            "gusano", 
            "gato", 
            "perro",
            "gusano"]

# metodo insert para insertar elementos
mascotas.insert(1, "Melvin") # agregando como 2do elemento
mascotas.append("Chanchito triste") # append permite agregar elementos al final de una lista
print(mascotas)

# eliminando elementos dentro de un listado
mascotas.remove("gato") # solo elemina el primer elemento llamado gato, si hay mas elementos llamados gato no los elimina
mascotas.pop() # elimina el ultimo elemento de un listado, no hay que pasarle nada
mascotas.pop(1) # si le pasamos el indice en donde se encuentra el elemento, lo elimina
del mascotas[0] # tambien permite eliminar un elemento pasandole el indice
mascotas.clear() # limpia o borra todo el listado
print(mascotas)
