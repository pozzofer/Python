def valores():
    num1 = 110
    num2 = 40
    resultado = num1 + num2
    return resultado

print(valores())    #funcion estatica : su result siempre va a ser el mismo

#para poder ultilizar una variables dentro o fuera de la funcion puedo usar la palabre reservada global
def valores():
    global num1
    global num2
    num1 = 110
    num2 = 40
    resultado = num1 + num2
    return resultado

print(valores())

resta = num1 - num2
print(resta)