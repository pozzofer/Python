lista = [1 , 3 , 2 , 4 , 5]

#funcion append
# se usa para agregar mas datos a una lista
lista.append(6)
print(lista)
lista.append('python')
print(lista)

#funcion insert 
#se usa para agregar dato a una lista pero en una posicion en ESPECIFICO
lista.insert(2 , 2.5) 
print(lista)
 



lista = [2 , 1 , 3 , 4 , 5]
#funcion count
#cuanta la cantidad de veces que aprarece un elemento dado
print(lista.count(5))

#funcion index
#sirve para buscar datos
print(lista.index(4))

#funcion sort
#sirve para ordenar la lista
lista.sort()
print(lista)

#funcion reverse
#sirve para acomodar la lista a la reversa
lista.reverse()
print(lista)




lista = ['python', 24 , 'fer' , 'matias' , 22]
 
#modificar datos de una lista
'''lista[3] = "Fer"
print(lista)
print(lista[3])'''

#funcion pop()
#se utiliza para eliminarel ultimo dato de una lista
lista.pop()
print(lista)
lista.pop()
print(lista)

#funcion remove
#elimina un dato en especifico de la lista
lista.remove('python')
print(lista)

