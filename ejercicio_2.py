#Escribir un programa que le pregunte al usuario una cantidad 
# a invertir, el interés porcentual anual y el número de años,
#  y muestre por pantalla el capital obtenido en la inversión
#  redondeado a dos decimales

cantidad_a_invertir=float(input("ingrese la cantidad a invertir"))
interes=float(input("ingrese el interes porcentual anual"))
cantidad_de_años=int(input("ingrese el numero de años"))

print("El capital obtenido en la inversion es" + str((cantidad_a_invertir*((interes/100)+1)**cantidad_de_años)))



