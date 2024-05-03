usuarios = [
    ["chanchito", 4 ],
    ["Beto", 1],
    ["pulga", 5]
]

# obtener solamente el nombre, transformaremos la lista para devolver un listado de nombres.
nombres = []
for usuario in usuarios:
    nombres.append(usuario[0])
print(nombres)
# se tomo la lista anterior, se iteró sobre ella y con append se fue agregando el primer elemento que es el de nombres en la lista vacía.

# forma mas elegante de hacer lo mismo de antes en 1 sola linea:
print()

# nombres [expresion for item in items]
nombres = [usuario[0] for usuario in usuarios]
print(nombres)
# de esta forma elegante, se hacen transformaciones a las listas, en una lista nueva se coloca la expresión a usar de otra lista
# en este caso necesitabamos solamente el primer elemento, se hace la iteracion for con el iterable usuario en la lista usuarios
# y se imprime

# filtrar
nombres = [usuario for usuario in usuarios if usuario[1] > 2]
print(nombres)

# se filtra por medio de condiciones
# podemos modificar las listas y filtrarlas.

nombres = [usuario[0] for usuario in usuarios if usuario[1] > 2] 
print(nombres)
# lista filtrada y transformada, se filtra para que nada mas muestre el indicie[0] o sea los nombres, y el indice [1] o sea el id
# solo muestre los que son mayores que 2