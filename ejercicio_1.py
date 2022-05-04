#Una panadería vende barras de pan a 3.49€ cada una. 
#El pan que no es el día tiene un descuento del 60%. 
#Escribe un programa que comience leyendo el número de barras vendidas que no son del día.
# Después tu programa debe mostrar el precio habitual de una barra de pan,
# el descuento que se le hace por no ser fresca y el coste final total.

barras_pan= int(input("ingresa el numero de barras que se vendieron pero que no son frescas"))
precio= 3.49
descuento = 0.6
coste_final = ((barras_pan*precio)-descuento)

print("el precio habitual de una barra de pan del dia " + str(precio*barras_pan))
print("el precio de una barra de pan que NO es del dia es" + str((precio*barras_pan)-descuento))
print("el precio de una barra de pan del dia, mas una que NO es del dia es" + str((precio*barras_pan)+((precio*barras_pan)-descuento)))