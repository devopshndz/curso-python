# ciclo for
# iterar una LISTA de elementos

for numero in range(int(input("escriba el numero para generar la lista: "))):
    print(numero, numero * 'Hola Mundo!')

# range() nos genera una lista (0,1,2,3,4), range() es un iterables.
# la variable numero va a tomar el valor de los elementos que se encuentran dentro del range(5) o sea 0,1,2,3,4

# for else, ejemplo de buisques en un array, vamos a buscar un numero en este ejemplo:

buscar = 3   
for numero in range(int(input("escriba el numero para generar la lista: "))):
    print(numero)
    if numero == buscar:
        print("encontrado", buscar)
        break # detiene nuestro codigo
else:
    print("No encontré el numero buscado") # Si se termina de iterar y no se encuentra el valor buscado este else se activa

# ejemplo de iterablñe con string:
for char in "Ultimate Python":
    print(char)
