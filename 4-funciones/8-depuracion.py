### depuracion en funciones
# se realiza un ejemplo de un codigo que está malo, cuando se corre el codigo arroja un resultado erroneo a lo que se le pide
# se va a hacer uso del depurador (insecto con play de la izquierda).
# al darle click al depurador, y escoger a archivo de python podemos acceder a la consola de depuración.
# agregamos punto rojo en la linea 13 el cual determina que ahí se va a detener el depurador para examinar que ocurre.
# vamos a ir aadelantando con el panel de botones de arriba 

def largo(texto): # calcular la longitud de caracteres
    resultado = 0
    for _ in texto:
        resultado += 1
    return resultado

print("Chanchito") # colocar el punto rojo a la izquierda para que el depurador se detenga
l = largo("Hola mundo")
print(l)