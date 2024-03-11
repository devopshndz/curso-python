"""Strings
"""

nombre_curso = "Ultimate python"
descripcion = """
Ultima Python,
Este curso contempla todos los detalles
que necesitas aprender para encontrar 
trabajo como derrollador.
""" 

print(nombre_curso, descripcion)

# funcion len: para medir la longitud de un string particular
print(len(nombre_curso))
print(nombre_curso[0]) # imprimir el primer caracter del string
print(nombre_curso[0:8]) # imprimir la palabra cortada, [0:8] significa que desde el primer indice, cuenta 8 indices mas, corta e imprime la palabra.
print(nombre_curso[:8]) # exactamente lo mismo que arriba
print(nombre_curso[9:]) # toma desde el indice 9 hasta el final del string
print(nombre_curso[:]) # imprime todo
