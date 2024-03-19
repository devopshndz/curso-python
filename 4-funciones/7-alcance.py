### alcance de las funciones

def saludar():
    saludo = "Hola mundo" # variable distinta
    print(saludo) # primero hay que definir una variable antes y luego llamarla

def saludaChanchito():
    saludo = "Hola Chanchito" # variable distinta
    print(saludo)

saludar()
saludaChanchito()
saludar()

# Buena practica: NO USAR VARIABLES GLOBALES, UTILIZAR SOLO VARIABLES EN CONTEXTOS, O SEA DENTRO DE FUNCIONES