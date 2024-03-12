# modulo math
import math # modulo matematico, de esta menera importamos modulos para llamarlos y trabajar con ellos.

print(round(1.3)) # devuelve el número mas cerca al numero que le pasamos, 1
print(round(1.7)) # 2
print(round(1.5)) # 2
print(abs(-77)) # valor absoluto, en positivo
print(abs(77))

# un módulo es un código escrito en python que se trae y se utiliza.
# módulo math

print(math.ceil(1.1)) # numero mas cercano hacia arriba
print(math.floor(1.99999)) # numero entero mas cercano hacia abajo
print(math.isnan(23)) # si el valor que estamos pasando no es un numero, arrojará un booleano, en este caso dará false porque si estamos pasando un numero
num = float("nan")
print(math.isnan(num)) # se coloca una variable nun con un float("nan") como ejemplo de que no se está pasando un numero. No le veo mucho uso a esto.
print(math.pow(4, 3)) # math.pow permite elevar un numero a la potencia agregada, en este ejemplo 4 es num y 3 es la potencia.
print(math.sqrt(25)) # sqrt saca la raiz cuadrada de un numero que pasemos

# documentación de math: https://docs.python.org/es/3.10/library/math.html
