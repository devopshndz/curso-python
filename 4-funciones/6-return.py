### Uso del return: obtener un resultado o algo y asignarselo a una variable para su uso posterior.

def suma(a, b):
    resultado = a + b
    return resultado # retorna el valor resultado, cada que se llame la funcion siempre tendrá este resultado

c = suma(1, 2)
d = suma(c, 3)
print(d)