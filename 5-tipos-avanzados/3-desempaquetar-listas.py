numeros = [1, 2, 3]
primero = numeros[0]
segundo = numeros[1]
tercero = numeros[2]
# esto es feo

primero, segundo, tercero = numeros # se asignan los valores de la lista a primero, segundo y tercero
print(primero, segundo, tercero)

# obtener el primer listado de la lista
primer, *otros = numeros
print(primer, otros)

numeros = [1, 2, 3, 4, 5, 6, 7]
primer, segundo, *otros = numeros
print(primero, segundo, otros)
primer, segundo, *otros, ultimo = numeros # ultimo toma el valor del ultimo elemento
print(primero, ultimo, otros)
primer, segundo, *otros, penu, ultimo = numeros # ultimo toma el valor del ultimo elemento, y penu el del penultimos
print(primero, penu, ultimo, otros)