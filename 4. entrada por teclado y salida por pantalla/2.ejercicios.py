#ejercicio 2

#PP  = (P1 + P2 P3)/3 PROM = (PP + 2*EP + 3*EF)/6
#DONDE = P1, P2, P3 : Practicas
#PP: promedio de practica
#PROM: promedio
#EP examen parcial
#EF: examen final

practica1 = float(input("este es el resultado de la practica 1: "))
practica2 = float(input("este es el resultado de la practica 2: "))
practica3 = float(input("este es el resultado de la practica 3: "))
examenParcial = float(input("este es el resultado del examen parcial: "))
examenFinal = float(input("este es el resultado del examen final: "))

#round() redondea el numero
PP = ((practica1 + practica2 + practica3) / 3)
print("Este es el valor de promedio de practica:", round(PP, 3))

PROM = ((PP + 2*examenParcial + 3*examenFinal)/6)
print("Este es el valor de el promedio: ", round(PROM, 3)) 

