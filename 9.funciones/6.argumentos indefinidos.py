'''como almacenar los parametros en una tupla o una lista
valores indefinidos: es cuando no se cuantos valores se le van a asignar a una funcion
se coloca un parametro indefinido y despues el progrsmsdor decidira cuantos le ingresa '''

def argumento(num): 
    return type(num)

print(argumento(5.66))
print(argumento(5))
print(argumento("fer"))

#al colocar el asterisco todos los argumentos que yo le pase a esa funcion van a ser almacenados en esa tupla

def argumento(*num): 
    return type(num)

print(argumento(1 , 2 , 3 , 4 , 5))

def argumento(*num):
    for i in num:
        print(i)

print(argumento(1 , 2 , 3 , 4 , 5))