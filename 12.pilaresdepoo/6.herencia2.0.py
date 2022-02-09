#que tipo de errores puede generar el uso de la herencia
#va a ha haber ciertos metodos que no se van a heredar completamente por lo cual va a haber que hacer procedimientos extra para que se herede de manera completa


#metodo super para metodo init
class Animales():
    def __init__(self , nombre):
        self.nombre = nombre

class Perro(Animales):
    def __init__(self , nombre , sonido):
        super().__init__(nombre) # se agrega esta condicion para que se herede completamente
        self.sonido = sonido     


perro = Perro('Firulais' , 'guau')
print(perro.nombre)
print(perro.sonido)



