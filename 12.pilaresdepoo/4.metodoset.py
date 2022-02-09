class A():
    def __init__(self):
        self._cuenta = 0
        self._contador = 0
    
    #metodo get
    @property #con esta palabre esta va a ser tomado como un metodo get que va a ser llamado como si fuera un atributo
    def cuenta(self):
        return self._cuenta #retorna el valor del atributo cuenta

    #metodo set 
    @cuenta.setter #(nombreatributo.palabrareservadasetter)
    def cuenta(self , cuenta): # (self , atributo que se va a cambiar)
        self._cuenta = cuenta

    #metodo get
    @property
    def contador(self):
        return self._contador

    #metodo set
    @contador.setter
    def contador(self , contador):
        self._contador = contador  

#metodo get se usa para acceder al atributo pero para poder modificar se valor vamos a utilizar el metodo set

a = A()
#print(a._contador) #incorrecto
print(a.cuenta) #manera correcta con metodo get (objeto.nombredel metodo())
print(a.cuenta)

#mofificar el valor del atributo
a._cuenta = 20 #metodo incorrecto
a.cuenta = 20  # manera correcta metodo set
print(a.cuenta)
a.contador  = 30
print(a.contador)
