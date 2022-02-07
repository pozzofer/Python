#ejercicio1
# diccionario = {"guatemala" : 'cuidad de guatemala' , 'el salvador' : 'san salvador' , 'honduras' : 'honduras' , 'nicaragua' : 'managua' , 'costa rica' : 'san jose' , 'argentina' : 'buenos aires' , 'españa' : 'madrid'}
#
# pais = str(input('nombrar un pais: '))
# if diccionario[pais] == pais:
#    print(diccionario.get(pais))
#else:
#    print('ese pais no se encuentra registrado en el sistema')
#
###################################################################################################3

#Review con Matias

#se instancia en memoria el dicionario que contiene 
# "pais" : "capital"
diccionario = {"guatemala" : 'cuidad de guatemala' , 'el salvador' : 'san salvador' , 'honduras' : 'honduras' , 'nicaragua' : 'managua' , 'costa rica' : 'san jose' , 'argentina' : 'buenos aires' , 'españa' : 'madrid'}
pais = str(input('nombrar un pais (clave): '))
#print("Debuggeando: print de parametros del if (que esta comparando?) :\n ",  diccionario[pais], "  ", pais)
if pais in diccionario:
    print("valor de diccionario en el if :\n ", diccionario.get(pais))
    print("valor de la clave: ",pais ," = ", diccionario.get(pais))
else:
    print('ese pais no se encuentra registrado en el sistema')
















'''
#ejercicio 2
diccionario = {1 : "casillas" , 15 : 'ramos' , 3 : 'pique' , 5 : 'puyol' , 11 : 'capdevila' , 14 : 'xabi alonso' , 16 : 'busquets'}
print(diccionario)

#print(diccionario.get(2))

jugadores = input('ingrese un numero: ')
diccionario.get(jugadores)
print(jugadores)
nombreJugador = input('refiere al jugador: ')
print(nombreJugador)

jugador = int(input('ingrese un numero: '))
(print(diccionario.get(jugador)))'''





