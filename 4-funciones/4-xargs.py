# Multiples argumentos a nuestras funciones.

def suma(*numeros): # el * permite tomar muchos valores en el parametro agregado en la funcion e iterar
    resultado = 0
    for numero in numeros:
        resultado += numero # va a tomar todos los numeros que agregamos y los va iterar y a sumar
    print(resultado) # importante la identación.

suma(2, 5, 5) # iterables
suma(2, 5)
suma(2, 4, 5, 6, 7)