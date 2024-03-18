# Funciones funcion()

def hola(): # --> nuestra propia funcion, siempre se debe agregar def, el nombre de la funcion y ():
    print("Hola mundo!")
    print("Ultimate Python!")

# para llamar la función:
hola() # se llama la funcion con el nombre y los ()


def identificacion(nombre, apellido): # --> el nombre de la variable dentro de la función iodentificación se llama parametro
    print("Hola mundo!")
    print(f"Bienvenido! {nombre}, {apellido}")

# para llamar la función:
identificacion("Alberto", "Hernandez") # argumento
identificacion("Chanchito", "feliz") # cuando estamos pasando un valor a la llamada de la función este valor se llama argumento
 
