# ciclos if

edad = int(input("escriba la edad: "))
if edad > 65:
    print("El usuario puede ver la película con un super descuento por ser viej@ decrepit@")
elif edad > 50:
    print("El usuario puede ver la película con descuento por adulto mayor")
elif edad > 17:
    print("El usuario puede ver la película")
else:
    print("El usuario no puede ver la película")
    print("Indicar al usuario que vaya a otro lado y no moleste")

print("Proceso finalizado")

# para tener en cuenta:
# al usar ciclos if, las evualuaciones se haran en orden, si al evaluar una acción esta da True, el resto de evaciaciones se omiten 
# el orden es sumamente imporanten a la hora de hacer ciclos if.
