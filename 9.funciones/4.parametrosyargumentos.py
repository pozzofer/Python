def suma(): #en esta funcion no se pueden cambiar los datos de la misma
     num1 = 20
     num2 = 30
     suma = num1 + num2
     return suma

print(suma())

#parametro son las variables que la funcion va a utilizar
#argumento son los valores de las variables que se colocan al llamar a la funcion

#por lo cual necesito una funcion que permita modicar sus datos:
def suma (num1 , num2): #parametros
    suma = num1 + num2
    return suma

print(suma(10 , 35)) #argumento