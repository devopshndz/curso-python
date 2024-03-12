# Aplicación sencilla de calculadora.
"""Pasos:
1- Agregar metodo de entrada de datos por usuario con input()
2- """

n1 = int(input("Ingrese el primer numero: "))
n2 = int(input("Ingrese el segunddo numero: "))
# input() se utiliza para agregar datos desde teclado, por defecto todo el dato que se agregue será un string, se debe pasar a ser int si se necesita que se agreguen numero enteros

suma = n1 + n2
resta = n1 - n2
multi = n1 * n2
div = n1 / n2

mensaje = f"""
Para los numeros {n1} y {n2},
el resultado de la suma es {suma}.
el resultado de la suma es {resta}.
el resultado de la suma es {multi}.
el resultado de la suma es {div}.
"""

print(mensaje)
