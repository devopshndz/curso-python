# crear calculadora interactiva.
# verificar si un numero antes, sino, decirle al usuario que ingrese un numero
# luego de eso pedirle al usuario que ingrese una operación 
# se le va a pedir al usuario que ingrese de nuevo otro numero
# mostrar los resultado
# el resultado se guardará como el primer numero y se le va a pedir al usuario que ingrese una operacion

print("""
Bienvenidos a la calculadora.
Para salir escribe salir cuando quieras
las operaciones son suma, resta, multi y div
""")
resultado = ""
while True:
    if not resultado:
        resultado = input("Ingrese numero: ")
        if resultado.lower() == "salir":
            break
        resultado = int(resultado)
    op = input("Ingresa operacion: ")
    if op.lower() == "salir":
        break
    n2 = input("Ingresa siguiente numero: ")
    if n2.lower() == "salir":
        break
    n2 = int(n2)
    if op.lower() == "suma":
        resultado += n2
    elif op.lower() == "resta":
        resultado -= n2
    elif op.lower() == "multi":
        resultado *= n2
    elif op.lower() == "div":
        resultado /= n2
    else:
        print("Operación no valida")
        break

    print(f"El resultado es {resultado}")
