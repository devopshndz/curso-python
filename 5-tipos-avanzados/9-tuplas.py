# tuplas
# lo mismo que una lista pero no la puedes modificar, no la puedes eliminar, quitar, hacer cosas con los elementos existentes.

numeros = (1, 2, 3)
print(numeros)

numeros = (1, 2, 3)+(4, 5, 6)
print(numeros)

# usaremos las tuplas cuando no queramos que se modifique accidentalemtne los elementos de un listado
punto = tuple([1 ,2]) # tuple convierte una lista en una tupla. Recibe cualquier tipo de dato que sea iterable.
print(punto)

menosNumeros = numeros[:2]
print(menosNumeros)

primero, segundo, *otros = numeros
print(primero, segundo, otros)

for n in numeros:
    print(n)