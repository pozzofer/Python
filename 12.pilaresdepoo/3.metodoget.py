class A():
    def __init__(self):
        self._cuenta = 0
        self._contador = 0
    
    @property #con esta palabre esta va a ser tomado como un metodo get que va a ser llamado como si fuera un atributo
    def cuenta(self):
        return self._cuenta
    
    @property
    def contador(self):
        return self._contador



a = A()
#print(a._contador) #incorrecto
print(a.cuenta) #manera correcta con metodo get (objeto.nombredel metodo())
print(a.cuenta)
