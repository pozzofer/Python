class Animales():
    def __init__(self , mensaje):
        self.mensaje = mensaje

    def hablar(self):
        print(self.mensaje)

class Perro(Animales):
    def hablar(self):
        print('yo hago guau')

class Pez(Animales):
    def hablar(self):
        print("yo no hablo")        

perro = Perro("guau")        
perro.hablar()

pez = Pez('nada')
pez.hablar()