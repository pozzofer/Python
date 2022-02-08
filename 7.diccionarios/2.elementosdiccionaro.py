diccionario = {'Nombre' : 'Fer' , 'Apellido' : 'Pozzo' , 'Estatura' : 1.60}

#nos permite ver claves y valores de manera sepada
print(diccionario)
#me muestras las llaves(claves) del dic
print(diccionario.keys())
#me muestra los valores del d
print(diccionario.values())

#imprimir una llave para  que muestra su valor
print(diccionario['Estatura'])

#agragar una clave y valor al dicc
diccionario["Peso"] = 50
print(diccionario)

#modificar el vaor existente
diccionario['Nombre'] = 'Fernanda'
print(diccionario)