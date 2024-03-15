# while o condiconal mientras que.

numero = 1 # vamos a duplicarlo hasta que este sea igual a 100
while numero < 100:
    print(numero)
    numero *= 2

# comando = ""
# while comando != "salir":
#     comando = input("$ ") # como si estuvieramos imprimiendo el codigo que la terminal
#     print(comando)

# loops infinitos: Cuando no tenemos una condicion de salida y por ende el loop no se corta.
# comentar el codigo anterior para probar este que sigue
while True:
    comando = input("$ ") # como si estuvieramos imprimiendo el codigo que la terminal
    print(comando)
    if comando.lower() == "salir":
        break