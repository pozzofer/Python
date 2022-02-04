#ejercicio 2 
lista = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10]

lista[4] = 5*2
print(lista)
print(lista[4])
lista[7] = 8*2
print(lista)
print(lista[7])
lista[9] = 10*2
print(lista)
print(lista[9])
 
print(lista)

#ejercicio 1
lista = [20 , 50 , "curso" , 'python' , 3,14]
print(lista)
dato = (input("escribe un dato para la posicion 1: "))
lista.insert(1 , dato)
print(lista)
dato2 = (input("escribe un dato para la posicion 2: "))
lista.insert(2 , dato2)
print(lista)


#####################################################
#conjuntos
'''va a ser una estructura en python que va a permitir a una list TENER DATOS agrupados, 
la diferencia va a ser que las listas van a tener datos igguales, en cambio un conjunto no acepta datos repetidos'''
conjunto = {1 , 2 , 3 , 4 , 5}
print(type(conjunto))

# set se encarga de crear los conjuntos
'''conjunto = set[(1 , 2 , 3 , 4 , 5)]
print(type(conjunto))'''



#metodos de conjuntos
conjunto = {1 , 2 , 2 , 3 , 4 , 5}
lista = [1 , 2 , 2 , 3 , 4 , 4]
print(lista)
#solo se van a mostrar los datos una vez aunque esten repetidos
print(conjunto)


#funcion add
#sirve para añadir un nuevo elemento
conjunto.add(20)
print(conjunto)

#funcion remove/discard
#elimina un elemento dado del conjunto
conjunto.remove(1)
print(conjunto)

#funcion pop
#sirve para eliminar cualquier elemento al azar
conjunto.pop()
print(conjunto)

#funcion update
#permite a añadir elementos iterables
conjunto.update([1 , 2 , 3])
print(conjunto)

#funcion clear
#deja el conjunto vacio
conjunto.clear()
print(conjunto)

######################################################3
#tuplas
#datos inmutables
tupla = (1 , 2 , 3 , 4 , 5)
tupla2 = (6 , 7 , 8)
print(tupla)
print(type(tupla))

#elementos de una tupla
print(tupla[2])
#debanado
print(tupla[0 : 3])
#suma
print(tupla + tupla2)



#ejercicio1
'''Escribir una tupla con los meses del año, luego, pide al usuario un numero, el que haya
ingresado es el mes que debe mostrar en la tupla
'''
tupla = ('enero' , 'febrero' , 'marzo' , 'abril' , 'mayo' , 'junio' , 'julio' , 'agosto' , 'septiembre' , 'octubre' , 'noviembre' , 'diciembre')
diferenciaMesIndiceTupla = 1
mes = int(input("escribe un numero: "))
print(tupla[mes - diferenciaMesIndiceTupla])


'''Escribir una tupla que tenga las letras del alfabeto.
Luego, debes pedir al usuario un número, el que haya ingresado, es la letra que debe imprimir el programa'''

tupla = ('a' , 'b' , 'c' , 'd' , 'e' , 'f')
difPosicion = 1
numero = int(input("escribe un numero: "))
print(tupla[numero - difPosicion])





























 




























