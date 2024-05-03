# tuplas
# listas ordenadas

numeros = [1, 3, 4, 6, 7, 10, 20]
numeros.sort() # ordena la lista de menor a mayor
print(numeros)

# ordernar al reves 
numeros.sort(reverse=True) # listado ordenado de mayor a menos
print(numeros)

# otro metodo, pero este crea otra nueva lista ordenada
numeros2 = sorted(numeros)
print("print con sort" ,numeros)
print("print con sorted", numeros2)

# order lista con otras listas adentro

usuarios = [
    [4, "chanchito"],
    [1, "Beto"],
    [5, "pulga"]
]

# lo va a ordenar si el primer elemento sea algo ordenable, lo ordena. De lo contrario no. hay que pasar una funcion:

def ordena(elemento):
    return elemento[1]

usuarios.sort(key=ordena)
print(usuarios)

# expresiones anonimas o expresiones lambdas

# print()
# def ordena(elemento):
#     return elemento[1]

usuarios.sort(key=lambda el: el[1] ,reverse=True)
print(usuarios)