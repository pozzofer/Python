class animales():
    def habla(self):
        print('soy un animal lol')

    def descripcion(self):
        print('yo soy un {}'.format(self.animal))


class perro(animales):#todos los atributos que estan en la clase animales van a estar en la clase perro
    pass              #clasehija(clasepadre)

class abeja(animales):
    def __init__(self , animal):
        self.animal = animal


animal = animales()
animal.habla()

perrito = perro()
perrito.habla()

abejorro = abeja("abeja")
abejorro.descripcion()