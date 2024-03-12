animal = "  chanCHito feliz  "
# upper es un metodo, el cual es una función que se encuentra dentro de un objeto (animal)
print(animal.upper()) # upper metodo  letras MAYUSCULAS
print(animal.lower()) # lower metodo letras minusculas
print(animal.capitalize()) # capitalize coloca la primera letra del string en mayuscula
print(animal.title()) # title coloca en mayusculas las primeras letras del string
print(animal.strip()) # strip remueve todos los espacios al comienzao y al final de string
print(animal.strip().capitalize()) # encadenamos los string, quitamos los espacios y coloca la primera letra mayuscula
# lstrip y rstrip quita los espacios de la izquierda y de la derecha de un string
print(animal.lstrip())
print(animal.rstrip())
print(animal.find("CH")) # devuelve el indice de caracteres que se está buscando
print(animal.find("cH"))
# si en la respuesta de la busqueda hay un -1 significa que la busqueda no encontró el caracter
print(animal.replace("nCH", "j")) # replace se usa para reemplazar una cadena de caracteres por otra
# si la encuentra, reemplaza, si no la encuentra vno hace el reemplazo. Siempre recibe 2 argumentos, la cadena de caracteres
# a buscar y la cadena de caracteres a reemplazar separados por , y entre ""
print("nCH" in animal) # in se usa para buscar si se encuentra una cadena de caracteres, retorna un boolean
print("nCH" not in animal) # not in hace lo contrario de in, pregunta si no se enceuntra en la cadena
