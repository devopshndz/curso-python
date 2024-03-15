# operadores logicos and, or, not
# and = dos condiciones que deben cumplirse
# or = dos o mas condiciones y al menos 1 de ellas es true
# not = negar el resultado de una operación.

gas = True
encendido = True
edad = 18

if gas or encendido:
    print("Puede avanzar")

if gas and encendido:
    print("Puede avanzar tambien")

if gas and (encendido or edad > 17):
    print("Puede avanzar")

### Operadores de corto circuito
# va a depender del operador con el que estemos trabajando 
# se va a evaluar de izquierda a derecha
    
if not gas and encendido and edad > 17:
    print("Puede avanzar")