class A():
    def __init__(self):
        self.contador = 0

    def incrementar(self):   #cada vez que yo mande a llamar a este metodo le va a incrementar 1 al contador
        self.contador += 1

    def cuenta(self):        #me va a retornar cual es el valor del contador
        return self.contador

print("objeto 1")
a = A()        
print(a.cuenta())
a.incrementar()
print(a.cuenta())
print(a.contador)  #esto no se debe hacer, se puede acceder al contador ya que no esta encapsulado pero no es correcto


#encapsulamineto refiere a un atributo que no puede ser acedido por fuera de la clase para eso le vamos a poder __ antes del atributo
# puede ser accedido desde la misma clase
class B():
    def __init__(self):
        self.__contador = 0

    def incrementar(self):   #cada vez que yo mande a llamar a este metodo le va a incrementar 1 al contador
        self.__contador += 1

    def cuenta(self):        #me va a retornar cual es el valor del contador
        return self.__contador




print("objeto 2")
b = B()
print(b.cuenta())
b.incrementar()
print(b.cuenta())
print(b.__contador) #esto va a dar error ya que el atributo esta encapsulado
