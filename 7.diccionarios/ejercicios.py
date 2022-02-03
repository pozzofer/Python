#ejercicio1
diccionario = {"guatemala" : 'cuidad de guatemala' , 'el salvador' : 'san salvador' , 'honduras' : 'honduras' , 'nicaragua' : 'managua' , 'costa rica' : 'san jose' , 'argentina' : 'buenos aires' , 'españa' : 'madrid'}

pais = str(input('nombrar un pais: '))
if diccionario[pais] == pais:
    print(diccionario.get(pais))
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





