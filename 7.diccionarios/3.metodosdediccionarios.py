diccionario = {1 : 2 , 2 : 3 , 3 : 4}
diccionario2 = {4 : 5 , 5 : 6}
print(diccionario)

#funcion pop
#va a recibir como parametro una clave y a esa clave la va a eliminar
diccionario.pop(3)
print(diccionario)

#metodo clear
#LIMPIA EL DICCIOnARIO, es decir, lo borra por completo
#diccionario.clear()
#print(diccionario)

#metodo get
#va a recibir un parametro(llave) y va a devolver el valor
print(diccionario.get(2))

#metodo setdefault
#sirve p agregar un valor
#recibe el valor de la lleva y su valor¿
diccionario.setdefault(4 , 5)
print(diccionario)

#metodo update
#sirve para actualizar un valor
#si hay una llave repetida solo va a quedar una
diccionario.update(diccionario2)
print(diccionario)

#metodo copy
#saca una copia del dic
#(llave , nuevo valor)
diccionario.copy()
print(diccionario)

