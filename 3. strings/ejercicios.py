#ejercicio 1
cadena = "te quiero solo como amigo"

print(cadena[0 : 2])
print(cadena[-3 :  ])
print(cadena[: : 2])
print(cadena[: : -1])
print(cadena[: : 1])
print(cadena + cadena[: : -1])


#ejercicio2
variable = "separado"

#metodo replace
cadena = "este es el uso del metodo replace"
print(cadena)
reemplazar = cadena.replace("e" , "E")
print(reemplazar)

palabra = "separado"
reemplazar = palabra.replace("" , ",")
print(reemplazar)
